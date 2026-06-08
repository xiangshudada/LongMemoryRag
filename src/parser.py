from dataclasses import dataclass, field
from typing import List, Optional
from pathlib import Path
import re


@dataclass
class Document:
    """统一文档数据结构"""
    content: str           # 文档完整内容
    file_path: str         # 文件路径（相对于memory根目录）
    metadata: dict = field(default_factory=dict)  # 元数据


def scan_memory_files(root_dir: str) -> List[str]:
    """递归扫描memory目录下所有.md文件，排除README.md和knowledge_index.md"""
    root_path = Path(root_dir)
    excluded_files = {"README.md", "knowledge_index.md", "_index.md"}
    result = []

    for md_file in root_path.rglob("*.md"):
        if md_file.name in excluded_files:
            continue
        result.append(str(md_file))

    return sorted(result)


def _extract_metadata_from_content(content: str) -> dict:
    """从文档内容中提取元数据（正则匹配头部字段）"""
    metadata = {}

    # 匹配 "服务:xxx" 格式
    service_match = re.match(r"服务[:：]\s*(.+)", content, re.MULTILINE)
    if service_match:
        metadata["service"] = service_match.group(1).strip()

    # 匹配 "版本:xxx" 格式
    version_match = re.search(r"^版本[:：]\s*(.+)", content, re.MULTILINE)
    if version_match:
        metadata["version"] = version_match.group(1).strip()

    # 匹配 "路径:METHOD /api/xxx" 格式
    path_match = re.search(r"^路径[:：]\s*(.+)", content, re.MULTILINE)
    if path_match:
        path_line = path_match.group(1).strip()
        # 尝试分离 HTTP方法 和 路径
        method_path_match = re.match(r"(GET|POST|PUT|DELETE|PATCH)\s+(.+)", path_line)
        if method_path_match:
            metadata["method"] = method_path_match.group(1)
            metadata["path"] = method_path_match.group(2).strip()
        else:
            metadata["path"] = path_line

    # 匹配 "描述:xxx" 格式
    desc_match = re.search(r"^描述[:：]\s*(.+)", content, re.MULTILINE)
    if desc_match:
        metadata["description"] = desc_match.group(1).strip()

    return metadata


def _extract_metadata_from_path(file_path: str, memory_root: str) -> dict:
    """从文件路径推断元数据"""
    metadata = {}
    rel_path = Path(file_path).relative_to(Path(memory_root))
    parts = rel_path.parts  # e.g. ('api_docs', 'user_service', 'v1', 'user_login.md')

    # 推断 service（从目录名，如 user_service -> user-service）
    if len(parts) >= 2:
        service_dir = parts[1]  # e.g. 'user_service'
        metadata["service"] = service_dir.replace("_", "-")

    # 推断 version（如果有 v1, v2 等目录）
    for part in parts:
        if re.match(r"^v\d+$", part):
            metadata["version"] = part
            break

    # 从文件名推断 method
    filename = rel_path.name  # e.g. 'POST _api_payment_create.md'
    method_match = re.match(r"^(GET|POST|PUT|DELETE|PATCH)\s+", filename)
    if method_match:
        metadata["method"] = method_match.group(1)

    return metadata


def parse_document(file_path: str, memory_root: str) -> Document:
    """
    解析单个Markdown文档，提取结构化元数据。
    元数据字段：
    - service: 服务名称（从文档内容或目录路径推断）
    - version: 版本号（从文档内容或目录路径推断）
    - method: HTTP方法（GET/POST/PUT/DELETE）
    - path: API路径
    - description: 接口描述
    """
    file_path_obj = Path(file_path)
    content = file_path_obj.read_text(encoding="utf-8")

    # 计算相对路径
    rel_path = str(Path(file_path).relative_to(Path(memory_root)))
    # 统一使用正斜杠
    rel_path = rel_path.replace("\\", "/")

    # 优先从内容中提取元数据
    metadata = _extract_metadata_from_content(content)

    # 从路径推断的元数据作为补充（仅填充内容中缺失的字段）
    path_metadata = _extract_metadata_from_path(file_path, memory_root)
    for key, value in path_metadata.items():
        if key not in metadata:
            metadata[key] = value

    return Document(
        content=content,
        file_path=rel_path,
        metadata=metadata,
    )


def parse_all_documents(memory_root: str) -> List[Document]:
    """解析memory目录下所有文档"""
    file_paths = scan_memory_files(memory_root)
    documents = []

    for fp in file_paths:
        try:
            doc = parse_document(fp, memory_root)
            documents.append(doc)
        except Exception as e:
            print(f"[WARNING] 解析文件失败 {fp}: {e}")

    return documents
