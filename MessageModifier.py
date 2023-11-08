def modify_string_message(start_byte, end_byte, new_string, string_message):
    # Modify the specified portion of the string using slicing
    start_index=start_byte*2
    end_index=end_byte*2+1

    modified_string = string_message[:start_index] + new_string + string_message[end_index + 1:]
    return modified_string

