x = linspace(0, 2*pi, 100);
y = sin(x);
plot(x, y);
% print('./plot/test.png', '-dpng')
waitfor(figure)