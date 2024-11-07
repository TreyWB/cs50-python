def main():
    fname = input("File name: ")
    
    fname = fname.lower()
    fname = fname.strip()
    ext = fname.split(".")
    ext[1] = "." + ext[1]
    
    type_lookup(ext[1])
    
def type_lookup(ext):
    match ext:
        case ".gif":
            print("image/gif")
        case ".jpg" | ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("File extension not recognized")
main()