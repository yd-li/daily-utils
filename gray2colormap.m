img = imread('d_0001.png');
[X, map] = rgb2ind(img, 65536);
graymap = rgb2gray(map);

rbmap = redbluecmap(100)
[m, n] = size(graymap);

for r = 1:m
    index = round(graymap(r, 1) * 10);
%     disp(index);
    graymap(r,:) = rbmap(index+1,:);
end

newimg = ind2rgb(X, graymap);
imshow(newimg);