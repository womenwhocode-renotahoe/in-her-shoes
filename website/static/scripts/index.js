$(function() {
  $("#content").dragend({
    afterInitialize: function() {
      this.container.style.visibility = "visible";
    },
    onSwipeEnd: function() {
      var first = this.pages[0],
          last = this.pages[this.pages.length - 1];

      $(".prev, .next").removeClass("deactivated");
      $(".nav li").removeClass("active");

      if (first === this.activeElement) {
        $(".prev").addClass("deactivated")
      };

      if (last === this.activeElement) {
        $(".next").addClass("deactivated")
      }

      $(".nav li").eq(this.page).addClass("active");

    }
  });

  $(".prev").click(function() {
    $("#content").dragend("right");
  });

  $(".next").click(function() {
    $("#content").dragend("left");
  });

  $(".button-menu").click(function() {
    var page = $(event.target).data("page");

    $("#content").dragend({
      scrollToPage: page
    });

    $(event.target).addClass("active");

  })

});