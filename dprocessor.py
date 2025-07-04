import os
from gazette_tracker.processor import find_gazette_pdf, extract_year_and_id, get_meta_data


BASE_DIR = os.path.expanduser("~/Desktop/gazette-archive")

def main():
    files = find_gazette_pdf(BASE_DIR)
    print("\n")
    print(len(files), "entries found ...\n")
    for path in files[:5]:
        meta = extract_year_and_id(path, BASE_DIR)
        if meta:
            meta_data = get_meta_data(meta["year"], meta["gazette_id"], BASE_DIR)
            if meta_data:
                wanted_fields = ["gazette_id", "date" , "description"]
                filtered_meta = {key: meta_data[key] for key in wanted_fields if key in meta_data}
                meta.update(filtered_meta)
            
            print(filtered_meta)
            print("\n")
            
            

if __name__ == "__main__":
    main()