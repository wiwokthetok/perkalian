import curses

def menu(stdscr, options):
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for idx, row in enumerate(options):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(options) // 2 + idx
            if idx == current_row:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, row)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return options[current_row]

def main(stdscr):
    stdscr.clear()
    curses.echo()

    stdscr.addstr("Masukkan angka pertama: ")
    num1 = float(stdscr.getstr().decode())

    curses.noecho()
    operasi = menu(stdscr, ["Kali (×)", "Bagi (÷)"])

    curses.echo()
    stdscr.clear()
    stdscr.addstr("Masukkan angka kedua: ")
    num2 = float(stdscr.getstr().decode())

    if operasi.startswith("Kali"):
        hasil = num1 * num2
    else:
        if num2 == 0:
            hasil = "Error: Tidak bisa bagi 0"
        else:
            hasil = num1 / num2

    stdscr.clear()
    stdscr.addstr(f"Hasil: {hasil}\n")
    stdscr.addstr("\nTekan tombol apa saja untuk keluar...")
    stdscr.getch()

curses.wrapper(main)
