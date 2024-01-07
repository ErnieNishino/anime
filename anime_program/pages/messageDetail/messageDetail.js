// pages/messageDetail/messageDetail.js
Page({
  /**
   * 页面的初始数据
   */
  data: {
    title: '',
    date: '',
    image: '',
    detail: ''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    const title = options.title || '';
    const date = options.date || '';
    const image = options.image || '';
    const detail = options.detail || '';

    this.setData({
      title,
      date,
      image,
      detail
    });
  },
});
