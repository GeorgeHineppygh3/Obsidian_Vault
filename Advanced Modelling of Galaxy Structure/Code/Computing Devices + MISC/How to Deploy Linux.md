---
s:: true
---
---
s:: true
---
---
s:: true
---
# What is the most efficient way to do it?


Deploying linux through the virtual machine is incredibly inefficient and slow and so there needs to be a way around it.

Link to guide for VM operation/Set up: [How to run GAX](../../MISC/Group%20Resources/How%20to%20run%20GAX.md) 

On the meeting I was unable to attend on the 8th February 2023 Steven showed Aden how to set up a linux machine that will link to VS-code. 

I asked Aden to create a guide of how he set it up for the group and he has done so in a message to the discord in the form of a .txt document.

### Aden how to:

```
Microsoft store > Download 'Ubuntu' 
Run Ubuntu
Gives prompt to install Linux component via 'https://aka.ms/wslinstall' can do this by running 'wsl --install' on Command Prompt (administrator)
Restart PC
launch Ubuntu (it should install Linux components)
Follow prompts (username is easiest to do with no special characters and all lowercase otherwise it might complain)
When doing password it wont show characters being input however will still input them, I don't think you can remove any characters so if you make a typo just try again when it prompts (input 'y')

To paste things into the linux terminal simply right-click onto the chat line (on the flickering white underscore) and it should paste what is on clipboard

At this point its setup and you have your linux terminal, you can access files currently on your pc (windows ones) I can't remember offhand how to do so but Steven suggested saving it directly into the linux terminal
Can also launch github desktop	 via the terminal and use as usual to my understanding

Installing git:
run 'sudo apt-get install git'

Cloning repository:
run 'git clone https://github.com/IntraClusterLight/gax.git'

This will prompt a login into github; due to the use of a VM terminal this will not be possible with the usual login of username + password
Input username as usual

Go onto github, Profile dropdown in top right > settings > Developer settings (very bottom) > Personal access tokens > Tokens (classic)

Note that online it suggests that you use fine-grained tokens however for me I could not get this to work at all on ubuntu and Steven said he has had issies with it before too so the classic token works best

Select 'generate new token (classic)', login on prompt, then tick all permissions and give an appropriate note for the token
(likely do not need to tick all permissions, however I do not know which ones we actually need and cba to find out so I just ticked all of them)
It will then give you a personal access token. SAVE THIS SOMEWHERE AS YOU CANNOT ACCESS THIS AGAIN AFTER AND WILL HAVE TO REMAKE THE TOKEN IF YOU FORGET

Copy the token and paste it into the password prompt (again just right click the flashing white underscore bit once, dont repeat click or press any other keys as it wont show up and will screw up the password)
If it doesnt paste correctly you can just press the up arrow key to bring back the git clone command line and redo it until you paste successfully 

After this it should tell you when the repositry has been cloned and thats as far as I've got so far, not had a chance to look into the rest of the linux code yet 


```
## Using Aden's method - WSL is fantastic

### Update 2023-02-13: have broken WSL - lmao you twat
