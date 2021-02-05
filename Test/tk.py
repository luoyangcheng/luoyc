wx.login({

      success: res => {

        // 发送 res.code 到后台换取 openId, sessionKey, unionId

        console.log(res.code);

        wx.request({

            url: 'http://localhost/mi/getopenID.php',

            data:{code:res.code},

          success:(res)=>{

              console.log(res.data.openid);

              console.log(this);

              this.globalData.openID=res.data.openid;

          }

        })

      }

    })
