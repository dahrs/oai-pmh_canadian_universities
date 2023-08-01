import re
import shutil
import datetime
from os import listdir
from os import makedirs
from os.path import isdir
from os.path import isfile


def url_2_path(a_url: str, dataset_dir: str = "./dataset/raw2") -> str:
    url_data = [el for el in a_url.split("/") if (el and "http" not in el and "oai" not in el and "request" not in el)]
    site_top_lvl_dom = [".com", ".org", ".net", ".int", ".edu", ".gov", ".mil",
                        ".ca", ".us", ".fr"
                        ]
    site_top_lvl_dom = "|".join(site_top_lvl_dom)
    url_data = [el for el in url_data if re.findall(rf"{site_top_lvl_dom}$", el)][0]
    url_data = reversed(url_data.split("."))
    a_path = "/".join(url_data)
    a_path = f"{dataset_dir}/{a_path}"
    if not isdir(a_path):
        makedirs(a_path)
    a_path = f"{a_path}/data"
    return a_path


def url_2_file_name(a_url: str, prefix_path: str = "") -> str:
    prefix_path = f"{prefix_path}/" if prefix_path else prefix_path
    url_data = [el for el in a_url.split("/") if (el and "http" not in el and "oai" not in el and "request" not in el)]
    site_top_lvl_dom = [".com", ".org", ".net", ".int", ".edu", ".gov", ".mil",
                        ".ca", ".us", ".fr"
                        ]
    site_top_lvl_dom = "|".join(site_top_lvl_dom)
    url_data = [el for el in url_data if re.findall(rf"{site_top_lvl_dom}$", el)][0]
    url_data = reversed(url_data.split("."))
    url_data = [el for el in url_data if el]
    a_file_name = "_".join(url_data)
    a_file_name = f"{prefix_path}{a_file_name}"
    return a_file_name


def url_2_path_default(out_path: str, site_url: str) -> str:
    out_f_path = url_2_file_name(site_url, prefix_path=out_path)
    return out_f_path


def make_readme(r_path: str, a_url: str, schema: str) -> None:
    # DEPRECATED fonction qui fait un ReadMe automatique
    name = "_".join(r_path.split("/")[3:-2])
    with open(f"{r_path}/README.{schema}.md", "w", encoding="utf-8") as md_f:
        md_f.write(f"#{name}\n\nOrigin: {a_url}\n\nExtraction date: {datetime.datetime.now()}\n")
    return


def make_readme_file(r_path: str, a_url: str, schema: str) -> None:
    # automatically make a README file
    name = r_path.split("/")[-1]
    with open(f"{r_path}.{schema}.README.md", "w", encoding="utf-8") as md_f:
        md_f.write(f"#{name}\n\nOrigin: {a_url}\n\nExtraction date: {datetime.datetime.now()}\n")
    return


def make_readme_default(out_p: str, site_url: str, extract_schema: str) -> None:
    make_readme_file(out_p, site_url, extract_schema)
    return


def overwrite_check(out_p: str, s_url: str = "", format_type: str = "") -> bool:
    if url_2_file_name(s_url) in out_p or not s_url:
        if not isfile(f"{out_p}.{format_type}.README.md"):
            return True
    return False


def get_files_paths(main_dir: str, name_elem_required: str = None, file_extension: [str, None] = None,
                    go_recursive: bool = False) -> tuple[list, list]:
    all_paths = [f"{main_dir}/{nn}" for nn in listdir(main_dir)]
    if name_elem_required:
        all_paths = [pp for pp in all_paths if name_elem_required in pp]
    dir_paths = [pp for pp in all_paths if isdir(pp)]
    extract_files = [pp for pp in all_paths if isfile(pp)]
    if file_extension:
        extract_files = [pp for pp in extract_files if file_extension in pp]
    readme_files = [pp for pp in all_paths if isfile(pp) and "README.md" in pp]
    if go_recursive:
        for dir_p in dir_paths:
            e_fls, r_fls = get_files_paths(dir_p, go_recursive)
            extract_files += e_fls
            readme_files += r_fls
    return extract_files, readme_files


def from_deprecated_to_new(out_path: str, a_url: str, a_schema: str) -> None:
    old_p = url_2_path(a_url)
    old_p_r = f"{old_p[:-4]}README.md"
    old_p = f"{old_p}.jsonl"
    new_p = url_2_file_name(a_url, out_path)
    new_p_r = f"{new_p}.{a_schema}.README.md"
    new_p = f"{new_p}.{a_schema}.jsonl"
    if isfile(old_p):
        shutil.copy(old_p, new_p)
    if isfile(old_p_r):
        shutil.copy(old_p_r, new_p_r)
    return
