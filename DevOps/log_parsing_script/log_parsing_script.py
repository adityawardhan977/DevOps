def parse_logs(file_name):
    error_logs = []
    warning_logs = []
    info_logs = []

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            if "ERROR" in line:
                error_logs.append(line)
            elif "WARNING" in line:
                warning_logs.append(line)
            elif "INFO" in line:
                info_logs.append(line)

    print("\n===== LOG SUMMARY =====")
    print("Errors  :", len(error_logs))
    print("Warnings:", len(warning_logs))
    print("Info    :", len(info_logs))

parse_logs(r"D:\MY_WORK\DevOps\log_parsing_script\sample_logs.txt")