---
s:: true
---

Hi guys, this took me forever so wouldn't want you guys wasting time on it now that I know how to do it:

In order to run the GAX code you need to have the` jaxlib` library which is unfortunately not available on windows. Instead to run the code a virtual Linux machine on your windows computer is required. Below details how to set this up and get the code to a working order.

Before starting make sure you have retrieved the files from the relevant links.

### You will need:

- At least 25 GB of space on your computer
- Decent amount of ram ideally 8GB + as I am running it on 4GB and it is quite slow
- Retrieve Virtual box and download it from here (Windows edition) - shorturl.at/lqtVW
- Retrieve Ubuntu boot file from here - shorturl.at/dpRT5

### Steps:

- make sure you have downloaded the `ubuntu.iso` file and you know where it is (ideally not downloads)
- Open and install `Oracle VM VirtualBox` (just keep clicking next until finish appears)
- Now you have the Open Virtual box program - Click the icon where it says new
- Then name your virtual device ( choose where you want the device to live [again not downloads put it somewhere specific])
- Under version you want to select `Ubuntu 64-bit` 
- Next page should say how many resources you should give the device - you can have a look in task manager to see how much CPU and Memory you use as a baseline - If not sure just give it half of the specs of your computer
- Next it should ask you how big it will make the 'virtual hard drive' - this needs way more than you think minimum 25GB - Put the hard drive storage in the same folder you have put everything else in
- Leave all the settings default
- It is going to tell you its going to format your drive but don't freak out its only formatting the new virtual drive it has created
- After this the virtual machine should have been created 
- go into settings and then display and give it some more video memory (otherwise it's so grainy)
- open the device by pressing start in the VM software
- navigate to Firefox and download VS-code from - shorturl.at/ghU13
- download the Git Repos onto your new device
- Open the Git repos in VS-code
- After opening the code it should prompt you to download the python and Jupyter libraries for VS-code
- After you have installed these navigate to the terminal and run `pip list`
- its should say something like "pip is not understood you can fix it by blah blah blah" run whatever it says and then pip install all the required libraries with: pip install `BLANK` 
	- numpy
	- matplotlib
	- jax
	- jaxlib
	- astropy
	- Any others that are not installed
- Navigate to multi Sérsic Jupyter notebook and run it (this should now work)

Any problems, speak to me.

Cheers,

George
