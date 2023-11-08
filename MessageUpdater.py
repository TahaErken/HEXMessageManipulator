import time
import floatCalculator
import endianChanger
import MessageModifier




def update_message(value1, value2):

    exampleMessage = "5743552FAA00000000D419A142AA9F354E41AA855E51402D8C3F4000000000000000000000000000016FA5E5B50000000000008fcc2A"  # 54 byte
    DataField1 = [floatCalculator.float_to_hex(value1),10,13] #10-13. bytelar
    DataField2 = [floatCalculator.float_to_hex(value2),14,17] #15-18. bytelar

    #if you would like to change some other BYTES write here similar to above exp.
    #if you would like to change Endian type :endianChanger.big_endian_to_little_endian(DataField2[0]))


    updated_message= MessageModifier.modify_string_message(DataField1[1],DataField1[2],DataField1[0],exampleMessage)
    updated_message= MessageModifier.modify_string_message(DataField2[1], DataField2[2], DataField2[0], updated_message)


    print("updated message", updated_message)
    return updated_message
