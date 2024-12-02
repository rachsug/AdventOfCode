def red_nosed_reports():
    f = open('day2_input.txt', 'r')
    data = f.read()
    
    lines_of_data = data.split('\n')

    safe_reports = 0
    res = 0
    unsafe_reports = []
    asc = False
    desc = False
    for report in lines_of_data:
        reports_list = report.split(' ')
        count = 1
        asc = False
        desc = False
        for i in range(len(reports_list)-1):
            prev_num = int(reports_list[i])
            next_num = int(reports_list[i+1])
            within_range = 1 <= abs(prev_num - next_num) <= 3
            if prev_num < next_num and within_range and not desc:
                count += 1
                asc = True
            elif prev_num > next_num and within_range and not asc:
                count += 1
                desc = True
            else:
                unsafe_reports.append(reports_list)
            if count == len(reports_list):
                safe_reports += 1
        res = safe_reports

    set_unsafe_reports = set(tuple(unsafe_report) for unsafe_report in unsafe_reports)
    list_unsafe_reports = [list(unsafe_report) for unsafe_report in set_unsafe_reports]
    safe_lists = set()

    for unsafe_report in list_unsafe_reports:
        for i in range(len(unsafe_report)):
            count = 1
            asc = False
            desc = False
            remove_level_list = unsafe_report[:i] + unsafe_report[i+1:]
            for new_list in range(len(remove_level_list)-1):
                prev_num = int(remove_level_list[new_list])
                next_num = int(remove_level_list[new_list+1])
                within_range = 1 <= abs(prev_num - next_num) <= 3
                if prev_num < next_num and within_range and not desc:
                    count += 1
                    asc = True
                if prev_num > next_num and within_range and not asc:
                    count += 1
                    desc = True
                if count == len(remove_level_list):
                    if tuple(remove_level_list) not in safe_lists:
                        safe_lists.add(tuple(remove_level_list))
                        print(unsafe_report, remove_level_list)
                        res += 1
                    break
            else: 
                continue
            break

    return print(res)

red_nosed_reports()