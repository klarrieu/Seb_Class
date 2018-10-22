import cIce as cic
import fFree as ff
import cIO as cio
import os


def main():
    logger = ff.logging_begin("icelog.log")
    client_orders = {"Jerry": 2, "Terry": 4, "Larry": 20, 'Barry': 1, 'Sherry': 3}  # add scoop numbers or modify client names
    ice = cic.Ice('rude')
    data_file = cio.WbMod(os.path.dirname(__file__) + "\\ice.xlsx", 0)

    col_client = "D"
    col_scoops = "E"
    col_size = "F"
    col_revenue = "G"
    row = 2

    for client in client_orders.keys():
        size, revenue = ice.dialogue(scoops=client_orders[client])
        logger.info("The shop manager takes notes for his tax statement.\n")
        row += 1
        data_file.write_data_cell(col_client, row, client)
        data_file.write_data_cell(col_scoops, row, client_orders[client])
        data_file.write_data_cell(col_size, row, size)
        data_file.write_data_cell(col_revenue, row, revenue)

    data_file.save_close_wb(os.path.dirname(__file__) + "\\ice.xlsx")
    ff.logging_end(logger)


if __name__ == "__main__":
    main()
