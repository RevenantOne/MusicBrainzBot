from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.set_window_position(2200, 0)

def wait(waitTime, pollFreq, cssSelector):
    try:
        # elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'profileinfo')))
        wait = WebDriverWait(driver, timeout=waitTime, poll_frequency=pollFreq)#, ignored_exceptions=['ElementNotVisibleException', 'ElementNotSelectableException'])
        w = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))
    except:
        print('Element not found.') 

def mbLogin():
    driver.get('https://test.musicbrainz.org/login')
    assert 'Log In - MusicBrainz' in driver.title

    loginUser = driver.find_element(By.ID, 'id-username')
    loginUser.send_keys('Kinxy_Bot')
    loginPass = driver.find_element(By.ID, 'id-password')
    loginPass.send_keys('mb')
    loginButton = driver.find_element(By.CSS_SELECTOR, '.buttons > button:nth-child(1)')
    loginButton.click()

    wait(10, 1, '.profileinfo')

def mbAddRelease():
    idCount = 13

    driver.get('https://test.musicbrainz.org/release/add')
    assert 'Add Release' in driver.title

    ### Release Information
    releaseTitle = driver.find_element(By.CSS_SELECTOR, '#name')
    releaseTitle.send_keys('The Best Kat')
    releaseArtist = driver.find_element(By.CSS_SELECTOR, 'input.name:nth-child(3)')
    releaseArtist.send_keys('265bae10-363f-4962-ba77-3c7dee29977e')
    # releaseArtistSearch = driver.find_element(By.CSS_SELECTOR, 'span.artist > img:nth-child(1)')
    # releaseArtistSearch.click()
    # releaseArtistConfirmation= driver.find_element(By.XPATH, '/html/body/ul[1]/li[1]/a/span')
    # releaseArtistConfirmation.click()
    ## Not need for new albums
    # releaseRGroup = driver.find_element(By.CSS_SELECTOR, '#release-group')
    # releaseRGroup.send_keys('Release Group Test')
    # releaseRGroupSearch = driver.find_element(By.CSS_SELECTOR, 'div.half-width:nth-child(1) > fieldset:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > span:nth-child(1) > img:nth-child(3)')
    # releaseRGroupSearch.click()
    # releaseRGroupConfirmation = driver.find_element(By.CSS_SELECTOR,'#ui-id-7 > li:nth-child(1)')
    # releaseRGroupConfirmation.click()
    releasePType = driver.find_element(By.CSS_SELECTOR, '#primary-type')
    selectPType = Select(releasePType)
    selectPType.select_by_visible_text('Album')
    releaseSType = driver.find_element(By.CSS_SELECTOR, '#secondary-types')
    selectSType = Select(releaseSType)
    selectSType.select_by_visible_text('DJ-mix')
    selectSType.select_by_visible_text('Remix')
    releaseStatus = driver.find_element(By.CSS_SELECTOR, '#status')
    selectStatus = Select(releaseStatus)
    selectStatus.select_by_visible_text('Bootleg')
    releaseLang = driver.find_element(By.CSS_SELECTOR, '#language')
    selectLang = Select(releaseLang)
    selectLang.select_by_visible_text('English')
    releaseScript = driver.find_element(By.CSS_SELECTOR, '#script')
    selectScript = Select(releaseScript)
    selectScript.select_by_visible_text('Latin')
    
    ### Release Event
    # ToDo: something to calculate fields from valid date formats
    releaseDateYear = driver.find_element(By.CSS_SELECTOR, '.partial-date-year')
    releaseDateYear.send_keys('2000')
    releaseDateMonth = driver.find_element(By.CSS_SELECTOR, '.partial-date-month')
    releaseDateMonth.send_keys('03')
    releaseDateDay = driver.find_element(By.CSS_SELECTOR, '.partial-date-day')
    releaseDateDay.send_keys('10')
    releaseCountry = driver.find_element(By.CSS_SELECTOR, '#country-0')
    selectCountry = Select(releaseCountry)
    selectCountry.select_by_visible_text('[Worldwide]')
    releaseLabel = driver.find_element(By.CSS_SELECTOR, '#label-0')
    releaseLabel.send_keys('Test Label')
    releaseLabelSearch = driver.find_element(By.CSS_SELECTOR, 'div.half-width:nth-child(1) > fieldset:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > span:nth-child(1) > img:nth-child(3)')
    releaseLabelSearch.click()
    wait(10, 1, '#ui-id-' + str(idCount)) #13  
    releaseLabelConfirmation = driver.find_element(By.CSS_SELECTOR, '#ui-id-' + str(idCount))
    releaseLabelConfirmation.click()
    releaseCatNo = driver.find_element(By.CSS_SELECTOR, '#catno-0')
    releaseCatNo.send_keys('1234567890')
    releaseBarcode = driver.find_element(By.CSS_SELECTOR, '#barcode')
    releaseBarcode.send_keys('712345678904')
    releasePackaging = driver.find_element(By.CSS_SELECTOR, '#packaging')
    selectPackaging = Select(releasePackaging)
    selectPackaging.select_by_visible_text('None')

    ### Additional Information
    infoAnnotation = driver.find_element(By.CSS_SELECTOR, '#annotation')
    infoAnnotation.send_keys('Test Annotation')
    infoDisambiguation = driver.find_element(By.CSS_SELECTOR, '#comment')
    infoDisambiguation.send_keys('Test Album')

    ### External Links
    linksAdd = driver.find_element(By.CSS_SELECTOR, '.value')
    linksAdd.send_keys('https://www.qobuz.com/')
    wait(10, 1, '.link-type')
    linksType = driver.find_element(By.CSS_SELECTOR, '.link-type')
    selectType = Select(linksType)
    selectType.select_by_visible_text('  download for free')

    idCount = 30 # No idea but it does


    ### Next button
    btnNext = driver.find_element(By.CSS_SELECTOR, '#release-editor > div:nth-child(7) > button:nth-child(4)')
    btnNext.click()

    ### Next Page ###

    ### Release Duplicates
    rdDoNotUse = driver.find_element(By.CSS_SELECTOR, 'div.no-label:nth-child(4) > label:nth-child(1) > input:nth-child(1)')
    if rdDoNotUse.is_displayed():
        rdDoNotUse.click()
        btnNext.click()

    ### Next Page ###

    ### Add Medium Window
    amTracklist = driver.find_element(By.CSS_SELECTOR, '#add-medium-parser > textarea:nth-child(3)')
    amTracklist.send_keys('1. Track 1 - Kinxy Kat 1:23\n2. Track 2 - Kinxy Kat 4:56\n3. Track 3 - Kinxy Kat 7:54')
    amAddMedium = driver.find_element(By.CSS_SELECTOR, 'button.positive:nth-child(2)')
    amAddMedium.click()

    ### Tracklist
    noTracks = 3 # Find a way to get this automatically
    tlFormat = driver.find_element(By.XPATH,'//*[@id="medium-format-new-4"]')
    selectFormat = Select(tlFormat)
    selectFormat.select_by_visible_text('Digital Media')
    # tlArtistEdit = driver.find_element(By.CSS_SELECTOR, '#track-row-new-4 > td:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > button:nth-child(1)')
    # tlArtistEdit.click()
    
    for i in range(noTracks):
        # tlArtist = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/fieldset/div/table/tbody/tr[' + str(1 + i) + ']/td[4]/table/tbody/tr/td[1]/span/input')
        # tlArtist.send_keys('265bae10-363f-4962-ba77-3c7dee29977e')        
        wait(10, 1, '/html/body/div[3]/div/div[3]/div[2]/fieldset/div/table/tbody/tr[' + str(1 + i) + ']/td[4]/table/tbody/tr/td[1]/span/img')  
        tlArtistSearch = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/fieldset/div/table/tbody/tr[' + str(1 + i) + ']/td[4]/table/tbody/tr/td[1]/span/img')
        tlArtistSearch.click()
        wait(10, 1, '#ui-id-' + str(idCount))
        print(str(idCount + i + (i * 15)) + " " + str(idCount))
        tlArtistConfirmation = driver.find_element(By.CSS_SELECTOR, '#ui-id-' + str(idCount)) # 30 46
        idCount = idCount + 16

        
        if tlArtistConfirmation.text != 'Kinxy Kat':
            tlArtistDirectSearch = driver.find_element(By.CSS_SELECTOR, '#ui-id-' + str(idCount - 5))
            tlArtistDirectSearch.click()
            wait(10, 1, '#ui-id-' + str(idCount - 3))
            tlArtistDirectConfirmation = driver.find_element(By.CSS_SELECTOR, '#ui-id-' + str(idCount - 3)) 
            tlArtistDirectConfirmation.click()
        else:
            tlArtistConfirmation.click()

        

    ### Next button
    btnNext.click()

    ### Next Page ###

    ### Recordings
    ### Next button
    btnNext.click()

    ### Next Page ###

    ### Edit Note
    enEditNote = driver.find_element(By.CSS_SELECTOR, '#edit-note-text')
    enEditNote.send_keys('Information taken from https://www.qobuz.com/\nPosted by Kinxy_Bot v.0.0.1\nhttps://github.con/project')



mbLogin()
mbAddRelease()

driver.quit()