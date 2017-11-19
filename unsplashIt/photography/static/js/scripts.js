var hoverSize = [100, 400];

$('img').hover(function() {
  $(this).css({
    height: hoverSize[0],
    width: hoverSize[1]
  });
}, function() {
  $(this).css({
    height: "",
    width: ""
  });
});
