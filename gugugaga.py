class GugaEncoder:
    """
    一个自定义编码器，用于将字符串编码为特定字符集表示，并能解码还原。
    编码基于五进制转换，并使用指定分隔符分隔字节单元。
    """

    def __init__(self, str_set: str = "咕嘎灵感菇", separator: str = "⭐"):
        """
        初始化编码器所需的字符集和分隔符。

        :param str_set: 字符集,用于从0~n映射具体字符
        :param separator: 编码中使用的分隔符
        """
        assert separator not in str_set, "分隔符不能在字符集中"

        self.str_set = str_set
        self.separator = separator
        self.len_charset = len(str_set)

        self.char_to_index = {char: idx for idx, char in enumerate(str_set)}
        self.index_to_char = {idx: char for idx, char in enumerate(str_set)}

    def encode(self, raw_str: str) -> str:
        """
        将输入字符串进行编码，输出由字符集组成的编码字符串。

        :param s: 原始字符串
        :return: 编码后的字符串
        """
        byte_data = raw_str.encode("utf-8")
        encoded = ""

        for byte in byte_data:
            digits = []
            if byte == 0:
                digits = [0]
            else:
                while byte > 0:
                    digits.append(byte % self.len_charset)
                    byte //= self.len_charset
            digits.reverse()

            encoded += "".join([self.index_to_char[d] for d in digits]) + self.separator

        return encoded.strip()[:-1]

    def decode(self, encoded: str) -> str:
        """
        将编码字符串解码还原为原始字符串。

        :param encoded: 编码后的字符串
        :return: 解码后的原始字符串 或 错误信息
        """
        if encoded == "":
            return ""
        part_list = encoded.split(self.separator)
        byte_list = []

        for part in part_list:
            num = 0
            for ch in part:
                digit = self.char_to_index[ch]
                num = num * self.len_charset + digit
            byte_list.append(num)

        return bytes(byte_list).decode("utf-8")


def codec_test():
    encoder = GugaEncoder()
    s = "我喜欢你。"
    print(f"原始字符串：{s}")
    encoded = encoder.encode(s)
    print(f"编码后：{encoded}")
    decoded = encoder.decode(encoded)
    print(f"解码后：{repr(decoded)}")


# 测试部分
if __name__ == "__main__":
    codec_test()
