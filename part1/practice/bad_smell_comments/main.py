class Unit:
    def move(self, field, x_coord: int, y_coord: int, direction, unit_fly: bool = True, unit_crawl: bool = False,
             unit_speed=1):

        if unit_fly and unit_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if unit_fly:
            unit_speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + unit_speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - unit_speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - unit_speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + unit_speed
        if unit_crawl:
            unit_speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + unit_speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - unit_speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + unit_speed

            field.set_unit(x=new_x, y=new_y, unit=self)
