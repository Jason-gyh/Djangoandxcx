// pages/dz/dz.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    text0: '\n',
    content:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var timestamp = Date.parse(new Date())/1000;
    console.log(timestamp)
    var that=this
    wx.request({
      url: 'http://v.juhe.cn/joke/content/list.php?sort=desc&page=15&pagesize=5&time='+timestamp+'&key=10524952bef9301b35f86d6f382c4961',
      success:function(res){
        console.log(res.data)
        that.setData({
          content:res.data.result.data
        })
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})