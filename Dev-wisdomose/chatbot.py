import asyncio
import discord
import random
#import openpyxl
import urllib
import urllib.request
import bs4
import time
import datetime

client = discord.Client()

# #토큰
token = "NTQ2OTQ1NzU1MjgyMTQ1MzAz.D0vvAA.Ocv4lMttirxqhYkshMJs1HRTKv4"

# 봇이 구동되었을 때 동작되는 코드.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    await client.change_presence(game=discord.Game(name="준서랑 화끈한 밤 ", type=1))

# 봇이 새로운 메시지를 수신했을때 동작되는 코드.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!커맨드'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await client.send_message(channel, '커맨드') #봇은 해당 채널에 '커맨드' 라고 말합니다.
    
    if message.content.startswith('!싼똥'):
        randomNum = random.randrange(1,4)
        if randomNum == 1 :
             await client.send_message(message.channel, embed=discord.Embed(title="걔 내 스타일아니야.", color=discord.Color.blue()))
        if randomNum == 2 :
             await client.send_message(message.channel, embed=discord.Embed(title="그 이름 그만 좀 말해 존1나 못생겨서 별로야", color=discord.Color.blue()))
        if randomNum == 3 :
             await client.send_message(message.channel, embed=discord.Embed(title="오늘은 좀 생각나는 걸?", color=discord.Color.blue()))
    
    #if message.content.startswith('!말배우기'):
    #    file = openpyxl

  #  if message.content.startswith('!롤'):
  #     await client.send_message(channel, '아 그 좆망겜 아직도 하는 사람있나요? 저도 안하는걸요..')
    ##else: #위의 if에 해당되지 않는 경우
        #메시지를 보낸사람을 호출하며 말한 메시지 내용을 그대로 출력해줍니다.
     ##   await client.send_message(channel, "<@"+id+">님이 \""+message.content+"\"라고 말하였습니다.")

    if message.content.startswith("!롤"):


        learn = message.content.split(" ")
        location = learn[1]

        enc_location = urllib.parse.quote(location)

        url = "http://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")


        ## 출력 셋 
             
        embedsolo = discord.Embed(
            title= "1",
            #description='',
            colour=discord.Colour.green()
        )

        ## 언랭크 확인 
        isUnrank = bsObj.find("div", {"class": "TierRankInfo"}).text.strip()
        
        ## 솔로랭크 파트 
        if('Unrank' in isUnrank):
        
            embedsolo.add_field(name='솔로랭크', value = '배치보셈;', inline=False)
        
        else:            
            ranktier = bsObj.find("div", {"class": "TierRank"}).text.strip()            
            lgpoint = bsObj.find("span", {"class": "LeaguePoints"}).text.strip()

            wins = bsObj.find("span", {"class": "wins"}).text.strip()
            losses = bsObj.find("span", {"class": "losses"}).text.strip()
            winratio = bsObj.find("span", {"class": "winratio"}).text.strip()
            
            rankout = ranktier + " / " + lgpoint + " / " + wins + " " + losses + "/ " + winratio
            embedsolo.add_field(name='솔로랭크', value= rankout, inline=False)

        await client.send_message(message.channel, embed=embedsolo)


        ## 출력 셋

        embed55 = discord.Embed(
            title= "2",
            #description='',
            colour=discord.Colour.red()
        )
        
        ## 언랭크 확인 
        isUnrank = bsObj.find("div", {"class": "sub-tier__info"}).text.strip()

        ## 자유랭크 파트 
        if('Unrank' in isUnrank):

            embed55.add_field(name='자유랭크', value = '배치보셈;' , inline=False)
        
        else:      
            ranktier = bsObj.find("div", {"class": "sub-tier__rank-tier"}).text.strip()
            lgpoint = bsObj.find("div", {"class": "sub-tier__league-point"}).text.strip()
            winratio = bsObj.find("div", {"class": "sub-tier__gray-text"}).text.strip()
            rankout = ranktier + " / " + lgpoint + " / " + winratio
            embed55.add_field(name='자유랭크', value = rankout, inline=False)
        
        await client.send_message(message.channel, embed=embed55)


    if message.content.startswith('!주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))


    if message.content.startswith('!타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]

        secint = int(Text)
        sec = secint

        for i in range(sec, 0, -1):
            print(i)
            await client.send_message(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)

        else:
            print("땡")
            await client.send_message(message.channel, embed=discord.Embed(description='타이머 종료'))


    if message.content.startswith('!제비뽑기'):
        channel = message.channel
        embed = discord.Embed(
            title='제비뽑기',
            description='각 번호별로 번호를 지정합니다.',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='끗')


        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip()) #입력한 명령어

        number = int(Text)

        List = []
        num = random.randrange(0, number)
        for i in range(number):
            while num in List:  # 중복일때만
                num = random.randrange(0, number)  # 다시 랜덤수 생성

            List.append(num)  # 중복 아닐때만 리스트에 추가
            embed.add_field(name=str(i+1) + '번째', value=str(num+1), inline=True)

        print(List)
        await client.send_message(channel, embed=embed)



    if message.content.startswith("!배그솔로"):

        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/"+enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        solo1 = bsObj.find("div", {"class": "overview"})
        solo2 = solo1.text
        solo3 = solo2.strip()
        channel = message.channel
        embed = discord.Embed(
            title='배그솔로 정보',
            description='배그솔로 정보입니다.',
            colour=discord.Colour.green())
        if solo3 == "No record":
            print("솔로 경기가 없습니다.")
            embed.add_field(name='배그를 한판이라도 해주세요', value='솔로 경기 전적이 없습니다..', inline=False)
            await client.send_message(channel, embed=embed)

        else:
            solo4 = solo1.find("span", {"class": "value"})
            soloratting = solo4.text  # -------솔로레이팅---------
            solorank0_1 = solo1.find("div", {"class": "grade-info"})
            solorank0_2 = solorank0_1.text
            solorank = solorank0_2.strip()  # -------랭크(그마,브론즈)---------

            print("레이팅 : " + soloratting)
            print("등급 : " + solorank)
            print("")
            embed.add_field(name='레이팅', value=soloratting, inline=False)
            embed.add_field(name='등급', value=solorank, inline=False)

            soloKD1 = bsObj.find("div", {"class": "kd stats-item stats-top-graph"})
            soloKD2 = soloKD1.find("p", {"class": "value"})
            soloKD3 = soloKD2.text
            soloKD = soloKD3.strip()  # -------킬뎃(2.0---------
            soloSky1 = soloKD1.find("span", {"class": "top"})
            soloSky2 = soloSky1.text  # -------상위10.24%---------

            print("킬뎃 : " + soloKD)
            print("킬뎃상위 : " + soloSky2)
            print("")
            embed.add_field(name='킬뎃,킬뎃상위', value=soloKD+" "+soloSky2, inline=False)
            #embed.add_field(name='킬뎃상위', value=soloSky2, inline=False)

            soloWinRat1 = bsObj.find("div", {"class": "stats"})  # 박스
            soloWinRat2 = soloWinRat1.find("div", {"class": "winratio stats-item stats-top-graph"})
            soloWinRat3 = soloWinRat2.find("p", {"class": "value"})
            soloWinRat = soloWinRat3.text.strip()  # -------승률---------
            soloWinRatSky1 = soloWinRat2.find("span", {"class": "top"})
            soloWinRatSky = soloWinRatSky1.text.strip()  # -------상위?%---------

            print("승률 : " + soloWinRat)
            print("승률상위 : " + soloWinRatSky)
            print("")
            embed.add_field(name='승률,승률상위', value=soloWinRat+" "+soloWinRatSky, inline=False)
            #embed.add_field(name='승률상위', value=soloWinRatSky, inline=False)

            soloHead1 = soloWinRat1.find("div", {"class": "headshots stats-item stats-top-graph"})
            soloHead2 = soloHead1.find("p", {"class": "value"})
            soloHead = soloHead2.text.strip()  # -------헤드샷---------
            soloHeadSky1 = soloHead1.find("span", {"class": "top"})
            soloHeadSky = soloHeadSky1.text.strip()  # # -------상위?%---------

            print("헤드샷 : " + soloHead)
            print("헤드샷상위 : " + soloHeadSky)
            print("")
            embed.add_field(name='헤드샷,헤드샷상위', value=soloHead+" "+soloHeadSky, inline=False)
            #embed.add_field(name='헤드샷상위', value=soloHeadSky, inline=False)
            await client.send_message(channel, embed=embed)



        

client.run(token)
