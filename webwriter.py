def write_html(messages):
    file = open("messages.html","w")
    html = []
    html.append('<html>\n<head>\n\t<meta http-equiv="Content-Type" content = "text/html" charset=UTF-8 >\n')
    html.append('\t<link rel="stylesheet" href="body.css">\n')
    html.append('\t<base href="../../"/>\n')
    html.append('\t<title>Beatriz Valladares</title>\n')
    html.append('</head>\n')
    html.append('\t<body class="_5vb_ _2yq _4yic">\n')
    html.append('\t<div class="clearfix _ikh"><div class="_4bl9"><div class="_li"><div id="bluebarRoot" class="_2t-8 _1s4v _2s1x _h2p _3b0a"><div aria-label="Facebook" class="_2t-a _26aw _5rmj _50ti _2s1y" role="banner"><div class="_2t-a _50tj"><div class="_2t-a _4pmj _2t-d"><div class="_218o"><div class="_2t-e"><div class="_4kny"><h1 class="_19ea" data-click="bluebar_logo"><a class="_19eb" data-gt="&#123;&quot;chrome_nav_item&quot;:&quot;logo_chrome&quot;&#125;" href="https://www.facebook.com/?ref=logo"><span class="_2md">Facebook</span></a></h1></div></div><div aria-label="Facebook" class="_2t-f" role="navigation"><div class="_cy6" id="bluebar_profile_and_home"><div class="_4kny"><div class="_1k67 _cy7" data-click="profile_icon"><a accesskey="2" data-gt="&#123;&quot;chrome_nav_item&quot;:&quot;timeline_chrome&quot;&#125;" class="_2s25 _606w" href="https://www.facebook.com/osniel.quintana" title="Perfil"><span class="_1qv9"><img class="_2qgu _7ql _1m6h img" src="https://scontent.ftpa1-1.fna.fbcdn.net/v/t1.0-1/p24x24/28577591_1570706753048642_5187107547097320467_n.jpg?_nc_cat=0&amp;_nc_ad=z-m&amp;_nc_cid=0&amp;oh=97807afcd09fe84405ca0235bff672b2&amp;oe=5C2336CD" alt="" id="profile_pic_header_100003279974709" /><span class="_1vp5">Osniel</span></span></a></div></div><div class="_4kny _2s24"><a class="_2s25 _cy7" href="index.html" title="Inicio">Inicio</a></div></div></div></div></div></div></div></div><div class="_3a_u"><div class="_3-8y _3-95 _3b0b"><div style="background-color: #3578E5" class="_3z-t"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAALVBMVEUAAAD///////////////////////////////////////////////////////+hSKubAAAADnRSTlMA7zDfcM8QYEC/gK+fj+TZazYAAABuSURBVAhbPc2xDQFhAAbQLyTKSxjgQvQKEeV12itELRIjiAVUNrCFUcQKf5yG5M2gwQLvJTlySZIprJNeDWWcPbDMFQy7NGy822cou8OJMEomhPNiUJNtd7PikbaAV/o/5y9nBvMkVfnu1T1J8gFhkEwPa1z8VAAAAABJRU5ErkJggg==" /></div><div class="_3b0c"><div class="_3b0d">Beatriz Valladares</div></div></div><div class="_4t5n" role="main">\n')

    for message in messages:
        html.append(write_message(message))

    html.append('\t</div></div></div></div></div>\n')
    html.append('\t</body>\n')
    html.append('\n</html>')
    toWrite = u''.join(html).encode('latin-1').strip()
    file.write(toWrite)
    file.close()


def write_message(message):
    sms = []
    sms.append('\t<div class="pam _3-95 _2pi0 _2lej uiBoxWhite noborder">\n')
    sms.append('\t\t<div class="_3-96 _2pio _2lek _2lel">\n')
    sms.append('\t\t\t' + message['sender_name'] + '\n')
    sms.append('\t\t</div>\n')
    sms.append('\t\t<div class="_3-96 _2let"><div><div></div><div>\n')
    sms.append('\t\t\t' + message['content'] + '\n')
    sms.append('\t\t</div><div></div><div></div></div></div>\n')
    sms.append('\t\t<div  class="_3-94 _2lem">\n')
    sms.append('\t\t\t' + message['timestamp_ms'])
    sms.append('\t\t</div></div>\n')
    return ''.join(sms)




