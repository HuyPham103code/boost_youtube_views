from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#read URLs video from file
viewCountFile = r"D:\CODE\Python\viewYoutube\view.txt"
videoFileName = r"D:\CODE\Python\viewYoutube\data.txt"

video_file = open(videoFileName)
videos = video_file.readlines()
print(videos)

#variables
NUMBER_OF_TAB = 4
NUMBER_OF_VIDEO = len(videos)
LOOP_TIME = 10
video_index = 0
tab_index = 0
tab_count = 1  #because when running the programme there is ready a tab
view_count = 0



#open driver
driver = webdriver.Chrome()
driver.get(videos[video_index])
sleep(3)

#play video
def play_video():
    #click play video
    button_play = driver.find_element(By.CLASS_NAME, 'ytp-large-play-button')
    button_play.click()
    sleep(LOOP_TIME)

#open new tab with video 2nd
def open_new_tab(index):
    driver.execute_script("window.open('{}', '_blank');".format(videos[index].strip()))

#switch window
def switch_window(index):
    driver.switch_to.window(driver.window_handles[index])

#start()

play_video()  # play first video
while True:
    video_index = (video_index + 1) % NUMBER_OF_VIDEO
    tab_index = (tab_index + 1) % NUMBER_OF_TAB

    if tab_count < NUMBER_OF_TAB:    # open new tab    0 1 2 3 
        tab_count +=1        
        open_new_tab(video_index)
    else:                            #change URL
        switch_window(tab_index)
        sleep(0.5)
        driver.get(videos[video_index])
   
    view_count += 1
    save_file = open(viewCountFile, "w")
    save_file.write(str(view_count))
    save_file.close()
    sleep(LOOP_TIME)


