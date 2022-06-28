function ys = year_score(f1, f2)
    x = double(f1);
    y = double(f2);
    fis = readfis('./fuzzyLogic/year.fis');
    ys = evalfis(fis, [x, y]);
end