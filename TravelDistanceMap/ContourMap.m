%load geoid
A = csvread('cities\62 StLouis.csv', 1,1);
%A = [-73.9387 40.6635 20;
%     -118.4108 34.0194 60;
%     -87.6818 41.8376 0;
%     -95.3909 29.7866 150];

axesm('mercator', 'MapLatLimit', [23 55], 'MapLonLimit', [-130 -66]);
geoshow(shaperead('usastatehi.shp', 'UseGeoCoords', true),'FaceColor', [.15 .5 .15]);
geoshow(shaperead('mexstates\mexstates.shp', 'UseGeoCoords', true),'FaceColor', [.15 .5 .15]);
geoshow(shaperead('Canada_Provinces\Canada_Provinces.shp', 'UseGeoCoords', true),'FaceColor', [.15 .5 .15]);
geoshow(shaperead('highways\intrstat.shp', 'UseGeoCoords', true));
tightmap;

lng_lin = linspace(min(A(:,1)), max(A(:,1)), 50);
lat_lin = linspace(min(A(:,2)), max(A(:,2)), 50);
[LNG, LAT] = meshgrid(lng_lin, lat_lin);

Z = griddata(A(:,1), A(:,2), A(:,3), LNG, LAT, 'cubic');

%contour(LAT,LNG,Z, 30);
%contourfm(geoid, geoidrefvec, -120:20:100, 'LineStyle', 'none');
contourm(LAT, LNG, Z, 'Fill', 'on');