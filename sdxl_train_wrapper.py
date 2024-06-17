try:
    from sdxl_train import setup_parser, train
    from library.train_util import read_config_from_file

    parser = setup_parser()
    args = parser.parse_args()
    args = read_config_from_file(args, parser)

    train(args)
    print("\n\033[1m✅ Done!")

except BaseException:
    import traceback
    import re
    from pygments import formatters, highlight, lexers

    tb = traceback.format_exc().split("\n")
    error_index = len(tb)
    for i, line in enumerate(tb):
        if re.match(r"^[A-Za-z-_]+Error:", line):
            error_index = i
            break
        tb_text = "\n".join(tb[:error_index])

        lexer = lexers.get_lexer_by_name("pytb", stripall=True)
        formatter = formatters.Terminal256Formatter()
        tb_colored = highlight(tb_text, lexer, formatter)

        print(f"\n{tb_colored}")
        if error_index < len(tb):
            tb_error = "\n".join(tb[error_index:])
            print(f"\033[0;31m\033[1m{tb_error}\n")
