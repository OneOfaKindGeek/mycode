#!/usr/bin/env python3
import wget
  
url = "https://cdn2.lamag.com/wp-content/uploads/sites/6/2019/04/avengers-endgame-disney-1068x601.jpg"

wget.download(url, '/home/student/static/')

print(url)
