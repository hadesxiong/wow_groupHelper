// app.js
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    wx.request({
      url: 'http://127.0.0.1:8000/base/WeChatAuth',
      success: function(res) {
        console.log(res)
      }
    })
    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId

      }
    })
  },
  globalData: {
    userInfo: null
  }
})
