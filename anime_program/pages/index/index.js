Page({
  data: {
    
  },
  gotoWeek: function (event) {
    const selectedDay = event.currentTarget.dataset.day;
    wx.navigateTo({
      url: `/pages/week/week?day=${selectedDay}`
    });
  }
});
