red = importdata("red.csv");

[xq,yq] = meshgrid(0:.2:54, 0:.2:27);
redq = griddata(red(:,1), red(:,2), sqrt(red(:,3)), xq, yq);

[C,h] = contourf(xq, yq, redq);
h.LevelStep = 0.02;
h.LineStyle = "none";
colormap(hot)