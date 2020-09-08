#网易云音乐weapi python解析

#每个请求csrf_token标识当前请求用户，访问用户权限信息时需要，为空表示游客

#用户登陆表单
csrf_token: "", password: "", phone: "", rememberLogin: "true"

#查询单曲信息

{csrf_token: "ed7548c6a6e...", id: "471385043", lv: -1, tv: -1}

#查询单曲评论
http://music.163.com/weapi/v1/resource/comments/R_SO_4_471385043?csrf_token=ed7548c6a6e40cf35dedc4652f6e99c0
{csrf_token: "ed7548c6a6e...", limit: "20", offset: "0", rid: "R_SO_4_4713...", total: "true"}

#查询用户歌单
http://music.163.com/weapi/user/playlist?csrf_token=eb87b1a8ba6c414935d953dee2cb52e2
{"uid":"64357970","wordwrap":"7","offset":"0","total":"true","limit":"36","csrf_token":"eb87b1a8ba6c414935d953dee2cb52e2"}
#查询听歌记录
http://music.163.com/weapi/v1/play/record?
{"uid":"64357970","type":"-1","limit":"1000","offset":"0","total":"true","csrf_token":"eb87b1a8ba6c414935d953dee2cb52e2"}
#查寻歌单歌曲列表
http://music.163.com/playlist?id=797678541
{"rid":"A_PL_0_66731285","offset":"0","total":"true","limit":"20","csrf_token":"85317d836b005ac492a95f4e3cd40077"}
#关键字搜索歌曲
