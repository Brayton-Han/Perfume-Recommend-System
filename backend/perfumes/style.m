function ys = style(f1, f2, f3, f4)
    qx = double(f1);
    gd = double(f2);
    ny = double(f3);
    ff = double(f4);
    fis = readfis('./fuzzyLogic/style.fis');
    ys = evalfis(fis, [qx, gd, ny, ff]);
end