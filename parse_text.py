class parse_coordinates():

    def parse_coord_text(file_name):
        x = []
        y = []
        z = []
        step = []

        with open(file_name) as f:
            lines = f.readlines()
            for line in lines:
                x_txt = 'X '
                y_txt = 'Y '
                z_txt = 'Z '
                step_txt = 'STEP '
                if x_txt in line:
                    lis = list(line[2:13])
                    if lis[0] == '+':
                        lis[0] = '-'
                    elif lis[0] == '-':
                        lis[0] = '+'
                    x_coord = ''.join(lis)
                    x += [f"{x_coord}"]
                if y_txt in line:
                    y_coord = line[2:13]
                    y += [f"{y_coord}"]
                if z_txt in line:
                    z_coord = line[2:13]
                    z += [f"{z_coord}"]
                if step_txt in line:
                    cur_step = line[5:6]
                    step += [cur_step]

                # Output a file for each coordinate.
                # Name the files after the step they are in.
        for i in range(0, len(x)):
            input_file = open(f'step{step[i]}.txt', 'w+')
            input_file.write(f'{x[i]}, {y[i]}, {z[i]}')
            input_file.close()
