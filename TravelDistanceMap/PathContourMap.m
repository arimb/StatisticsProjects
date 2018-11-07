cities = readtable('cities.csv', 'ReadRowNames', true);
files = dir('paths/');

for i = 1:length(files)-2-40
    file = files(i+2+40);
    name = extractBefore(file(1).name,strfind(file(1).name,'.'));
    disp(file(1).name);
    path = csvread(strcat('paths\', file(1).name), 1,0);
    A = csvread(strcat('cities\', file(1).name), 1,1);

    
    title(name);
    axesm('mercator', 'MapLatLimit', [23 55], 'MapLonLimit', [-130 -66]);
    geoshow(shaperead('usastatehi.shp', 'UseGeoCoords', true),'FaceColor', [.15 .5 .15]);
    geoshow(shaperead('shapefiles\mexstates\mexstates.shp', 'UseGeoCoords', true),'FaceColor', [.15 .5 .15]);
    geoshow(shaperead('shapefiles\Canada_Provinces\Canada_Provinces.shp', 'UseGeoCoords', true),'FaceColor', [.15 .5 .15]);
    
    scatterm(path(:,1), path(:,2), (path(:,3)).^(1/2), [.8 0 .6]);
    
    geoshow(shaperead('shapefiles\highways\intrstat.shp', 'UseGeoCoords', true), 'LineWidth', 0.2);
    tightmap;

    scatterm(cities{name, 'Lat'}, cities{name, 'Lng'}, 40, 'black', 'filled');

    lng_lin = linspace(min(A(:,1)), max(A(:,1)), 50);
    lat_lin = linspace(min(A(:,2)), max(A(:,2)), 50);
    [LNG, LAT] = meshgrid(lng_lin, lat_lin);
    Z = griddata(A(:,1), A(:,2), A(:,3), LNG, LAT, 'cubic');

    colormap(hot)
    caxis([0, max(A(A(:,3)<max(A(:,3)),3))]);
    cnt = contourm(LAT, LNG, Z, 'LineWidth', 3, 'LevelStep', 2);
    colorbar('Location', 'southoutside');
    
    saveas(gcf, strcat('img\', name, '.png'));
    clf;
end