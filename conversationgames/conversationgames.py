import discord
from redbot.core import commands, Config
from random import randint

BaseCog = getattr(commands, "Cog", object)


class ConversationGames(BaseCog):
    """Conversation games"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=763123)
        default_global = {
            "wyr": [
                "...always be 10 minutes late or always be 20 minutes early?",
                "...lose all of your money and valuables or all of the pictures you have ever taken?",
                "...be able to see 10 minutes into your own future or 10 minutes into the future of anyone but yourself?",
                "...be famous when you are alive and forgotten when you die or unknown when you are alive but famous after you die?",
                "...go to jail for 4 years for something you didn’t do or get away with something horrible you did but always live in fear of being caught?",
                "...accidentally be responsible for the death of a child or accidentally be responsible for the deaths of three adults?",
                "...your shirts be always two sizes too big or one size too small?",
                "...live in the wilderness far from civilization or live on the streets of a city as a homeless person?",
                "...the general public think you are a horrible person but your family be very proud of you or your family think you are a horrible person but the general public be very proud of you?",
                "...live your entire life in a virtual reality where all your wishes are granted or in the real world?",
                "...be alone for the rest of your life or always be surrounded by annoying people?",
                "...never use social media sites / apps again or never watch another movie or TV show?",
                "...have an easy job working for someone else or work for yourself but work incredibly hard?",
                "...be the first person to explore a planet or be the inventor of a drug that cures a deadly disease?",
                "...have a horrible short term memory or a horrible long term memory?",
                "...be completely invisible for one day or be able to fly for one day?",
                "...be locked in a room that is constantly dark for a week or a room that is constantly bright for a week?",
                "...be poor but help people or become incredibly rich by hurting people?",
                "...live without the internet or live without AC and heating?",
                "...have a horrible job, but be able to retire comfortably in 10 years or have your dream job, but have to work until the day you die?",
                "...find your true love or a suitcase with five million dollars inside?",
                "...be able to teleport anywhere or be able to read minds?",
                "...die in 20 years with no regrets or die in 50 years with many regrets?",
                "...be feared by all or loved by all?",
                "...be transported permanently 500 years into the future or 500 years into the past?",
                "...never be able to use a touchscreen or never be able to use a keyboard and mouse?",
                "...be able to control fire or water?",
                "...have everything you eat be too salty or not salty enough no matter how much salt you add?",
                "...have hands that kept growing as you got older or feet that kept growing as you got older?",
                "...be unable to use search engines or unable to use social media?",
                "...give up bathing for a month or give up the internet for a month?",
                "...donate your body to science or donate your organs to people who need them?",
                "...go back to age 5 with everything you know now or know now everything your future self will learn?",
                "...relive the same day for 365 days or lose a year of your life?",
                "...have a golden voice or a silver tongue?",
                "...be able to control animals (but not humans) with your mind or control electronics with your mind?",
                "...sell all of your possessions or sell one of your organs?",
                "...lose all of your memories from birth to now or lose your ability to make new long term memories?",
                "...be infamous in history books or be forgotten after your death?",
                "...never have to work again or never have to sleep again (you won’t feel tired or suffer negative health effects)?",
                "...be beautiful / handsome but stupid or intelligent but ugly?",
                "...get one free round trip international plane ticket every year or be able to fly domestic anytime for free?",
                "...be balding but fit or overweight with a full head of hair?",
                "...be able to be free from junk mail or free from email spam for the rest of your life?",
                "...be fluent in all languages and never be able to travel or be able to travel anywhere for a year but never be able to learn a word of a different language?",
                "...have an unlimited international first class ticket or never have to pay for food at restaurants?",
                "...see what was behind every closed door or be able to guess the combination of every safe on the first try?",
                "...live in virtual reality where you are all powerful or live in the real world and be able to go anywhere but not be able to interact with anyone or anything?",
                "...never be able to eat meat or never be able to eat vegetables?",
                "...give up watching TV / movies for a year or give up playing games for a year?",
                "...always be able to see 5 minutes into the future or always be able to see 100 years into the future?",
                "...super sensitive taste or super sensitive hearing?",
                "...be a practicing doctor or a medical researcher?",
                "...be married to a 10 with a bad personality or a 6 with an amazing personality?",
                "...never be able to drink sodas like coke again or only be able to drink sodas and nothing else?",
                "...be a reverse centaur or a reverse mermaid/merman?",
                "...have constantly dry eyes or a constant runny nose?",
                "...be a famous director or a famous actor?",
                "...not be able to open any closed doors (locked or unlocked) or not be able to close any open doors?",
                "...give up all drinks except for water or give up eating anything that was cooked in an oven?",
                "...have to read aloud every word you read or sing everything you say out loud?",
                "...have whatever you are thinking appear above your head for everyone to see or have absolutely everything you do live streamed for anyone to see?",
                "...be put in a maximum security federal prison with the hardest of the hardened criminals for one year or be put in a relatively relaxed prison where wall street types are held for ten years?",
                "...have a clown only you can see that follows you everywhere and just stands silently in a corner watching you without doing or saying anything or have a real life stalker who dresses like the Easter bunny that everyone can see?",
                "...kill one innocent person or five people who committed minor crimes?",
                "...have a completely automated home or a self-driving car?",
                "...work very hard at a rewarding job or hardly have to work at a job that isn’t rewarding?",
                "...be held in high regard by your parents or your friends?",
                "...be an amazing painter or a brilliant mathematician?",
                "...be reincarnated as a fly or just cease to exist after you die?",
                "...be able to go to any theme park in the world for free for the rest of your life or eat for free at any drive through restaurant for the rest of your life?",
                "...be only able to watch the few movies with a rotten tomatoes score of 95-100% or only be able to watch the majority of movies with a rotten tomatoes score of 94% and lower?",
                "...never lose your phone again or never lose your keys again?",
                "...have one real get out of jail free card or a key that opens any door?",
                "...have a criminal justice system that actually works and is fair or an administrative government that is free of corruption?",
                "...have real political power but be relatively poor or be ridiculously rich and have no political power?",
                "...have the power to gently nudge anyone’s decisions or have complete puppet master control of five people?",
                "...have everyone laugh at your jokes but not find anyone else’s jokes funny or have no one laugh at your jokes but you still find other people’s jokes funny?",
                "...be the absolute best at something that no one takes seriously or be well above average but not anywhere near the best at something well respected?",
                "...lose the ability to read or lose the ability to speak?",
                "...live under a sky with no stars at night or live under a sky with no clouds during the day?",
                "...humans go to the moon again or go to mars?",
                "...never get angry or never be envious?",
                "...have free Wi-Fi wherever you go or be able to drink unlimited free coffee at any coffee shop?",
                "...be compelled to high five everyone you meet or be compelled to give wedgies to anyone in a green shirt?",
                "...live in a house with see-through walls in a city or in the same see-though house but in the middle of a forest far from civilization?",
                "...take amazing selfies but all of your other pictures are horrible or take breathtaking photographs of anything but yourself?",
                "...use a push lawn mower with a bar that is far too high or far too low?",
                "...be able to dodge anything no matter how fast it’s moving or be able ask any three questions and have them answered accurately?",
            ],
            "nhie": [
                "...watched the Ghostbusters remake.",
                "...wanted to be one of the Kardashians.",
                "...watched Spongebob Squarepants.",
                "...cried during a Pixar movie.",
                "...had a crush, or man crush, on Ron Swanson.",
                "...'cleaned up' by piling everything into a closet.",
                "...sung karaoke.",
                "...watched the 'Gangnam Style' music video.",
                "...had a crush on someone from 'Full House'.",
                "...watched an episode of 'Gilmore Girls'.",
                "...pretended to know a stranger.",
                "...worn sleepwear and pretended it was clothing.",
                "...said 'excuse me' when there was no one around.",
                "...scared myself in a mirror.",
                "...missed a high five.",
                "...heard someone else doing it.",
                "...sang in the shower.",
                "...blamed farts on an animal.",
                "...secretly wished I were a wizard at Hogwarts.",
                "...slept in regular clothing.",
                "...had a nightmare about zombies chasing me.",
                "...pretended to laugh at a joke I didn't get.",
                "...been scared of clowns.",
                "...thought a cartoon character was hot.",
                "...faked being sick so I could play video games.",
                "...liked Star Wars more than Star Trek.",
                "...tried out to be an extra in a movie.",
                "...scored over 100 while bowling.",
                "...used an Instant Pot.",
                "...played Candy Crush.",
                "...won a game of Scrabble.",
                "...made a duck face when taking a selfie.",
                "...looked out the car's passenger seat window and imagined it was a scene from a music video.",
                "...actually laughed out loud when typing 'lol'.",
                "...reread an email immediately after sending it.",
                "...daydreamed about being on a talk show and what I'd talk about.",
                "...Googled my own name to see what comes up.",
                "...pretended I was running from zombies while on a run.",
                "...sat in the shower.",
                "...tried something I saw on Pinterest.",
                "...ugly cried for no reason.",
                "...creeped on someone I just met on social media.",
                "...thought about how a loved one could identify me if my face was horribly disfigured in an accident.",
                "...answered someone 'left' or 'right' without thinking, because I have a 50/50 chance of being right.",
                "...been out of the country.",
                "...regifted a gift card.",
                "...traveled out of state by myself.",
                "...flown in a helicopter.",
                "...been on stage in front of a crowd.",
                "...lied in a job interview.",
                "...stalked a crush.",
                "...sung karaoke.",
                "...agreed with something Donald Trump said.",
                "...thought about what type of dog I would be.",
                "...watched children's cartoons I'm too old for.",
                "...lost sunglasses that I was already wearing.",
                "...locked my keys in my car.",
                "...not tipped at a restaurant.",
                "...given money to a homeless person.",
                "...tried to look at the sun.",
                "...bungee-jumped.",
                "...had surgery.",
                "...jumped out of a plane.",
                "...made a wish at a fountain.",
                "...accidentally eaten a bug.",
                "...cut someone in line.",
                "...stayed up all night.",
                "...read a single Harry Potter book.",
                "...been inside of a library.",
                "...lied about my age.",
                "...shot a gun.",
                "...had a cavity.",
                "...been mini golfing.",
                "...seen an elephant in real life.",
                "...been to Disney World.",
                "...bought clothing online.",
                "...had someone draw a caricature of me.",
                "...owned an Xbox.",
                "...spent hours watching funny videos on Youtube.",
                "...seen Titanic.",
                "...met a celebrity.",
                "...thought a movie was better than the book.",
                "...voted.",
                "...owned a watch.",
                "...ridden a skateboard.",
                "...learned how to play a musical instrument.",
                "...seen snow.",
                "...finished a Sudoku puzzle.",
                "...Googled something so I'd know how to spell it.",
                "...cheated on a test.",
                "...cried watching Homeward Bound.",
                "...licked a frozen pole.",
                "...had gum in my hair.",
                "...taken a horrible picture on picture day.",
                "...been a bully.",
                "...wanted to be a superhero.",
                "...been scared of the dark.",
                "...had trouble sleeping after watching a scary movie.",
                "...stayed up all night.",
                "...been to a sleepover.",
                "...had a birthday party.",
                "...cried at school.",
                "...sang on a stage.",
                "...performed in a talent show.",
                "...killed ants with a magnifying glass.",
                "...dropped Mentos into Coke or Pepsi.",
                "...eaten something on a dare.",
                "...used the excuse 'my dog ate my homework'.",
                "...sucked my thumb.",
                "...believed my toys had feelings.",
                "...watched Blue's Clues.",
                "...been terrified of a theme park ride.",
                "...been to a haunted house.",
                "...dressed up as a zombie for Halloween.",
                "...been sent to the principle's office.",
                "...done an Easter Egg Hunt.",
                "...built a fort with blankets.",
                "...fallen off a bike.",
                "...played video games all day.",
                "...stolen money from a sibling's piggy bank.",
                "...wished I had bunk beds.",
                "...played Pokemon.",
                "...been on a family road trip.",
                "...named a stuffed animal.",
                "...used training wheels.",
                "...eaten only candy for dinner.",
                "...stayed in character all day.",
                "...lied about being related to someone on tv.",
                "...written notes on the desk to use during a test.",
                "...tried to sign a permission slip for my parents.",
                "...stolen a friend's story and pretend it happened to me.",
                "...thrown something out of the school bus window.",
                "...lied about staying after school and went somewhere else.",
                "...hopped seats on the school bus.",
                "...accidentally sharted.",
                "...forgotten the punchline of a joke.",
                "...sang a song out loud and messed the lyrics.",
                "...walked in on someone in the bathroom.",
                "...had someone walk in on me in the bathroom.",
                "...sent a text to the wrong person.",
                "...tried to pass a silent fart, but it came out loud instead.",
                "...tripped in public.",
                "...wet the bed after childhood.",
                "...accidentally pooped my pants.",
                "...attempted martial arts moves while by myself.",
                "...drove over a curb.",
                "...mistaken a man for a women or vice versa.",
                "...laughed so hard, I peed my pants.",
                "...picked a wedgie in public.",
                "...called the wrong person, but pretended I meant to call them.",
                "...gone into the wrong restroom.",
                "...been so freaked to be outside at night, that I ran back in.",
                "...lost my swimwear bottoms.",
                "...had diarrhea at a friend's house.",
                "...broken a piece of furniture by sitting on it.",
                "...arrived somewhere late and had everyone staring at me.",
                "...had food stuck in my teeth all day.",
                "...walked around with my zipper down.",
                "...bought a children's toy for myself, as an adult.",
                "...recorded video of myself singing or dancing.",
                "...been caught picking my nose.",
                "...gotten something stuck in my nose.",
                "...greeted someone I thought was someone else.",
            ],
            "truths": [
                "Have you ever been in a police car, and if so, why?",
                "Who has the best voice in the server?",
                "Have you ever fallen in love with your best friend?",
                "When was the last time you peed your pants?",
                "Have you ever done something that you wish you apologized for when you had the chance?",
                "Who here is the hopeless romantic?",
                "How many people have you kissed?",
                "Have you ever kissed anyone before?",
                "What's the biggest number of crushes you've had at one time?",
                "Do you fall in love easily?",
                "What's the most embarrassing thing in your web history?",
                "Have your ever fantasized about anyone here?",
                "What's the stupidest thing you've done for a crush?",
                "Have your parents ever given you the 'birds and bees' talk?",
                "What do you look for in a partner?",
                "Do you have a crush on anyone here?",
                "What's the drunkest you've ever been?",
                "Have you ever kissed someone without permission?",
                "Where is your ideal first date?",
                "If you could give up happiness to never be sad, would you?",
                "Who would you want to spend 24 hours locked in a room with, and what would you do?",
                "If you could give up happiness to never be sad, would you?",
                "How old were you when you had your first kiss?",
                "Do you have someone you miss alot, but don't want to think about? why?",
                "What's the most embarrassing thing that's happened when you asked someone out?",
                "When was the last time you felt truly alive?",
                "Do you have a crush on someone? If so, who?",
                "How old is the oldest person you've dated?",
                "Do you simp for any fictional characters, and if so, who?",
                "What dating advice would you give your younger self?",
                "Who's the most attractive person you know?",
                "Have you ever practiced kissing on something/someone?",
                "Would you ever consider being in an open relationship?",
                "What's the naughtiest thing you've done in public?",
                "What's one habit your partner has that annoys you?",
                "Which two people here would make the best couple?",
                "Do you have trust issues?",
                "Do you love your partner?",
                "Who is/was your longest crush?",
                "Do you still have feelings for an ex?",
                "Why did you break up with your last partner, and who broke up with who?",
                "What is your favorite thing about your partner?",
                "Have you ever been caught checking someone out?",
                "If you had to kill one person here, who would it be?",
                "Has your partner ever embarrassed you?",
                "Who here do you want to cuddle with the most?",
                "Who's your 'celebrity crush'?",
                "What's the most disgusting prank you've ever played?",
                "Who here acts the most desperate?",
                "Do you think you have a chance at love?",
                "Who do you miss seeing the most?",
                "What's the most embarrassing thing you've done on a date?",
                "Who was your best partner and why?",
                "Why did you stop liking your previous crush?",
                "Out of the last three people you texted, if you had to kiss one of them who would you pick?",
                "Who from here would you date and why?",
                "Have you ever fallen in love with your best friend?",
                "What is your favourite anime?",
                "How old is the youngest person you've dated?",
                "What's the first thing you would do if you found out you could become invisible?",
                "What's the first letter of your crush's name?",
                "Who here would be the worst person to date?",
                "What's the stupidest thing you've done in front of someone you liked?",
                "Who here do you want to kiss the most?",
                "Who is your ex?",
                "How many people have you kissed?",
                "Why did you break up with your last partner, and who broke up with who?",
                "Did/Do you know that someone admired/s you?",
                "Have you ever had a fantasy that wasn't exactly 'legal'?",
                "Would you ever get back with an ex?",
                "If you had to describe your body to someone else, what would you say?",
                "Would you break up with someone over text?",
                "When was the last time you were daydreaming with someone you admire?",
                "Have you ever had a secret relationship? If so, with who?",
                "Who do you secretly think is hot?",
                "What's the weirdest thing you've done for your partner?",
                "What's your least favorite feature about yourself?",
                "What's one habit your partner has that annoys you?",
                "What's your ideal person to date like?",
                "Do you stalk anyone on social media, and if so, who?",
                "Have you ever considered cheating?",
                "Have you ever thought of cheating on your partner?",
                "What are some of your turn-ons and turn-offs?",
                "If you could give up happiness to never be sad, would you?",
                "Who's more attractive, you or your best friend?",
                "What's your trick for getting attention from a crush?",
                "Is it true that you have more than 4 exes?",
                "What's the riskiest thing you've done?",
                "Have you ever taken a picture of someone hot in public?",
                "Do you have a crush on anyone here?",
                "What's something that you find cute that you think is underrated?",
                "Have you ever been in a police car, and if so, why?",
                "Whose voice do you like the most?",
                "Have you ever had crush on your teacher?",
                "Do you love the person you're playing this with?",
                "Who's the last person you simped for?",
                "What's the biggest age difference of a crush you've had?",
                "In the group, who do you think fits the dumb role?",
            ],
            "dares": [
                "Set your crush's profile picture as your profile picture.",
                "Flirt with {name} poorly in text and send screenshots of it to you.",
                "Send a screenshot of your search history of last 2 days.",
                "Send the most recent photo of your gallery.",
                "Send your ugliest selfie.",
                "Text flirt and then send “I love you” to a someone already in a relationship (not married) and screenshot his/her reaction",
                "Send a romantic message to someone of your own gender and screenshot their response",
                "Send a video of you dancing.",
                "Call me and sing a song for me.",
                "Send a voice message saying that you love me in 3 romantic ways.",
                "Be my one day boyfriend or girlfriend.",
                "Write your and my name in your status for 1 day.",
                "Propose to me in the most sensual way possible.",
                "Send love letter through email to your class teacher.",
                "Select one mobile number blindfolded from your contacts and send one breakup message to him/her. Screenshot the response.",
                "Give a deep explanation of one item in front of you.",
                "Paint your fingernails blindfolded with a pencil. Show us the result.",
                "Do a prank call to your mother and tell “I’m expecting a baby soon”. Screenshot the response.",
                "Send me the last message you received from your crush.",
                "Make a voice call to me and sing rhymes.",
                "Make a video call to me and perform belly dance.",
                "Open your gallery, close your eyes, scroll randomly and select one picture and send it to me.",
                "Send a text message to your crush blindfolded.",
                "Put my picture as your mobile wallpaper for three days.",
                "Send a selfie of yours while keeping your finger in your nose.",
                "Call to any random number and do non-stop conversation for 2 minutes.",
                "Send me the message of your first message that sends to me.",
                "Make a video call to me and do 20 situps continuously.",
                "Send next five text messages to your friends using your elbow only.",
                "Wear your dress upside down and send that picture to me.",
                "Send any message using only emojis.",
                "Call someone and say nothing.",
                "Send five photo from your gallery.",
                "I’ll give you a person's contact information and send a romantic message to that person.",
            ],
        }
        self.config.register_global(**default_global)

    @commands.command(aliases=["wyr"])
    @commands.bot_has_permissions(embed_links=True)
    async def wouldyourather(self, ctx):
        """Would you rather?"""

        strings = await self.config.wyr()
        mn = len(strings)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.title = "Would you rather.."
        embed.description = strings[i]
        await ctx.send(embed=embed)

    @commands.command(aliases=["nhie"])
    @commands.bot_has_permissions(embed_links=True)
    async def neverhaveiever(self, ctx):
        """Never have I"""

        strings = await self.config.nhie()
        mn = len(strings)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.title = "Never have I ever.."
        embed.description = strings[i]
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def truth(self, ctx, *, user: discord.Member):
        """Ask a truth question to users!"""

        # Set author
        author = ctx.message.author

        # Get and pick random string
        strings = await self.config.truths()
        mn = len(strings)
        rs = randint(0, mn - 1)

        # Get and pick random user
        mn2 = len(ctx.guild.members)
        rp = randint(0, mn2 - 1)
        name = ctx.guild.members[rp].mention

        # Build Embed
        embed = discord.Embed()
        embed.title = f"{author.name} asked {user.name}"
        embed.description = strings[rs].format(name=name)
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def dare(self, ctx, *, user: discord.Member):
        """Dare someone!"""

        # Set author
        author = ctx.message.author

        # Get and pick random string
        strings = await self.config.dares()
        mn = len(strings)
        rs = randint(0, mn - 1)

        # Get and pick random user
        mn2 = len(ctx.guild.members)
        rp = randint(0, mn2 - 1)
        name = ctx.guild.members[rp].mention

        # Build Embed
        embed = discord.Embed()
        embed.title = f"{author.name} dared {user.name}"
        embed.description = strings[rs].format(name=name)
        await ctx.send(embed=embed)
