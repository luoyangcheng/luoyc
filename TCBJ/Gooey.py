from gooey import Gooey, GooeyParser


@Gooey(program_name="简单的实例")
def main():
    parser = GooeyParser(description="第一个示例!")
    c = parser.add_argument('请输入', widget="TextField")  # 文件输入框
    parser.add_argument('日期', widget="DateChooser")  # 日期选择框
    args = parser.parse_args()  # 接收界面传递的参数
    for i in range(5):
        a = i
        print(a, c)


if __name__ == '__main__':
    main()