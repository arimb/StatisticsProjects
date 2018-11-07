files = dir('paths/');

for i = 1:length(files)-2
    file = files(i+2);
    name = extractBefore(file(1).name,strfind(file(1).name,'.'));
    disp(file(1).name);
    A = csvread(strcat('paths\', file(1).name), 1,0);
    
    
    title(name);
    axesm('mercator', 'MapLatLimit', [23 55], 'MapLonLimit', [-130 -66]);
    geoshow(shaperead('usastatehi.shp', 'UseGeoCoords', true),'FaceColor', [.15 .5 .15]);
    geoshow(shaperead('shapefiles\mexstates\mexstates.shp', 'UseGeoCoords', true),'FaceColor', [.15 .5 .15]);
    geoshow(shaperead('shapefiles\Canada_Provinces\Canada_Provinces.shp', 'UseGeoCoords', true),'FaceColor', [.15 .5 .15]);
    
    scatterm(A(:,1), A(:,2), (A(:,3)).^(1/3), 'red');
    
    geoshow(shaperead('shapefiles\highways\intrstat.shp', 'UseGeoCoords', true), 'LineWidth', 0.2);
    tightmap;

    saveas(gcf, strcat('path_img\', name, '.png'));
    clf;
end