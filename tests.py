from functions.get_files_info import get_files_info

def test_get_files_info_current_dir():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)

def test_get_files_info_pkg():
    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

def test_get_files_info_bin_dir():
    result = get_files_info("calculator", "bin")
    print("Result for 'bin' directory:")
    print(result)

def test_get_files_info_outside_dir():
    result = get_files_info("calculator", "../")
    print("Result for outside directory:")
    print(result)

if __name__ == "__main__":
    print("Running all tests...\n")

    test_get_files_info_current_dir()
    print("\n" + "-"*50 + "\n")

    test_get_files_info_pkg()
    print("\n" + "-"*50 + "\n")

    test_get_files_info_bin_dir()
    print("\n" + "-"*50 + "\n")

    test_get_files_info_outside_dir()
    print("\n" + "-"*50 + "\n")