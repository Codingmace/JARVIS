from pywebcopy import save_webpage

baseUrl = 'https://windows10spotlight.com/page/'
for i in range(1, 2, 1):
    #url = baseUrl + str(i)
   # download_folder = str(i)
    
    kwargs = {'project_name': 'Widows_Spotlight'}

  #  save_webpage(url, download_folder, **kwargs)

    save_webpage('https://windows10spotlight.com/sitemap.xml','2', **kwargs)
