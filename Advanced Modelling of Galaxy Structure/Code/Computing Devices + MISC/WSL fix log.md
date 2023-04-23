---
s:: true
---
---
s:: true
---
---
s:: true
---

# 2023-02-14

Began using WSL and had success with executing the code. Built understanding until created python file (Documentation: [gax_fits.py](../Code%20description/Python%20files/gax_fits.py.md) ) which functions are called from into testing Jupyter notebook (Documentation [Borge_test.ipynb](../../../PDF%20exports/Borge_test.ipynb.md)). 

After creating function to read in images into composite multiband arrays (`Read_M_band(file_name)`) decided wanted to attempt running a small loop by transferring the `.fits` files into the folder structure within ubuntu. 

First attempt: tried dragging and dropping all $146,000$ files from the `D:` drive to the ubuntu `/home/borge/face_on_spiral_objects` - unsurprisingly this didn't work and seemingly only some of the files transferred leaving approximately 67,000 files in the `face_on_spiral_objects` folder.

After doing this any subsequent attempts to transfer files failed due to the write protection in the ubuntu drives.


In order to leave a complete file system inside the ubuntu folder I went in via the terminal to the folder and added write privileges to the folder and files and then removed them. 

After this I then mounted the `D:` drive to copy over the `.tgz` files into the ubuntu directory. The `.tgz` files were then found there. 

After this I then decided to extract the `.tgz` files  inside the ubuntu folder.
![Pasted image 20230214140211.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230214140211.png)

figure shows the ubuntu destination folder with 4/5 band `.tgz` files in (human error not computer) with sub folder `face_on_spiral_objects` which contains the extraction from the `_ga.tgz` file.
![Pasted image 20230214140424.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230214140424.png)
figure shows the ubuntu sub folder with the extraction inside it - everything set to read only

after this I wanted to rename the file to G_band or something more sensible - tried to do this with the mv command but had no success.

after doing this extraction could not extract any other `.tgz` files:
tried running
```
tar zxvf face_on_spiral_objects_ia.tgz
```
but it returns
![Pasted image 20230214141248.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230214141248.png)

I then tried changing the write privileges of everything in the folder but it did not work.

I then returned to VS-code to find:
![Pasted image 20230214141354.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230214141354.png)


## What to do to fix it:

### Options:
1. wait for dad
2. rebuild WSL

## What have we done since?

identified that have run out of inodes for the cdrive mount - need to format the Linux drive

formatting will take place 2023-02-15 12:00 ish - 
success and all files saved so 


# no issues in rebuild!!!!

===============================================================

# 2023-02-15

This worked until I tried to install conda through Linux with the following:

`$ wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh`

returning this:

![Pasted image 20230216125914.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216125914.png)

After this I changed the permissions of the downloaded file so that it can execute.

`borge@Borge:~$ chmod +x Anaconda3-2019.10-Linux-x86_64.sh`

after this I then executed the file with

`borge@Borge:~$ sh ./Anaconda3-2019.10-Linux-x86_64.sh`

returning

![Pasted image 20230216130327.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216130327.png)
I then confirmed the location; which returned:

![Pasted image 20230216130504.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216130504.png)

and now VS-code returns the error:
![Pasted image 20230216130533.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216130533.png)

===============================================================

`df` returns:

![Pasted image 20230216130943.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216130943.png)

`ls -l` in destination folder returns:
![Pasted image 20230216131100.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216131100.png)

and `ls -l` in Conda folder returns:

![Pasted image 20230216131158.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216131158.png)

## Thoughts from Borge:

```
Could not remove or rename /home/borge/conda/pkgs/pango-1.42.4-h049681c_0tvjgx1st/pkg-pango-1.42.4-h049681c_0.tar.zst.  Please remove this file manually (you may need to reboot to free file handles)

Could not remove or rename /home/borge/conda/pkgs/python-3.7.4-h265db76_1gbpm3rry/pkg-python-3.7.4-h265db76_1.tar.zst.  Please remove this file manually (you may need to reboot to free file handles)

Could not remove or rename /home/borge/conda/pkgs/gevent-1.4.0-py37h7b6447c_0iaofrsfx/pkg-gevent-1.4.0-py37h7b6447c_0.tar.zst.  Please remove this file manually (you may need to reboot to free file handles)

``` 

This seems to be the main problem - will go into files and remove manually


## Thoughts from AI:

given error message AI returns:
![Pasted image 20230216132822.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216132822.png)
then asking what may have halted the install returns:

![Pasted image 20230216132903.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216132903.png)

on next attempt will bare the advice in mind


===============================================================

tried unregistering WSL and starting again this time with installing Conda right away following:

- http://mmb.irbbarcelona.org/molywood/tutorials/windows_sub
one thing to note for this method when going through it with dad is to ignore the sh and just run: `./Anaconda3-2019.10-Linux-x86_64.sh` instead of `sh ./Anaconda3-2019.10-Linux-x86_64.sh`

but this meant that Conda was used as the main python path and as a result Jax would not work.

had to do the same thing again:

# when the Jupyter doesn't like pip use : 
# `sudo apt-get update` 
# this will update the source and stop the issue



# 2023-02-16 18:50 

- have got WSL working again without putting in any of my own personal notebook or `.py` files 
- will now try installing Conda
- have now installed Conda and nothing has broken WOOOOOOOOO
- now need to create a Conda environment form the `environment.yml` file - how exactly not sure
- says Conda is not found?
- running creating Conda environment directly in ubuntu
- ![Pasted image 20230216191338.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230216191338.png)
- has been swirling for ages - not sure how to end the process either - feel like this should be quicker

# 20:00

- came back after dinner to massive failure and now VS-code is unable to start with error: [WSL was interrupted unexpectedly] - was with friends so didn't have time to screenshot


# 2023-02-17 10:00

- turned computer on and ubuntu opened saying:
- ![Pasted image 20230217101515.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217101515.png)
- Wait cancel that that is the wrong ubuntu

# WE ARE USING UBUNTU 20.04

- VScode opens the directories but says:
- ![Pasted image 20230217101101.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217101101.png)
- going to select interpreter: [CONDA]
- it works...?
- ran test notebook successfully using the Conda interpreter


## 2023-02-17 16:19

- trying to create the conda environment in the terminal with:
- ![Pasted image 20230217162005.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217162005.png)
- ![Pasted image 20230217162026.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217162026.png)
- taking ages on this step
- ![Pasted image 20230217162357.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217162357.png)
- seems like it just takes a while
- ![Pasted image 20230217163140.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217163140.png)
- its doing something
- errored again:
```

    Traceback (most recent call last):
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/exceptions.py", line 1074, in __call__
        return func(*args, **kwargs)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda_env/cli/main.py", line 78, in do_call
        exit_code = getattr(module, func_name)(args, parser)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda_env/cli/main_create.py", line 102, in execute
        result[installer_type] = installer.install(prefix, pkg_specs, args, env)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda_env/installers/conda.py", line 32, in install
        unlink_link_transaction.execute()
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 244, in execute
        self.verify()
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/common/io.py", line 88, in decorated
        return f(*args, **kwds)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 221, in verify
        self.prepare()
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 213, in prepare
        stp.neutered_specs)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 288, in _prepare
        for prec, pcrec in zip(link_precs, pkg_cache_recs_to_link))
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 288, in <genexpr>
        for prec, pcrec in zip(link_precs, pkg_cache_recs_to_link))
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/gateways/disk/read.py", line 100, in read_package_info
        paths_data = read_paths_json(epd)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/gateways/disk/read.py", line 170, in read_paths_json
        data = json.load(paths_json)
      File "/home/borge/anaconda3/lib/python3.7/json/__init__.py", line 296, in load
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
      File "/home/borge/anaconda3/lib/python3.7/json/__init__.py", line 348, in loads
        return _default_decoder.decode(s)
      File "/home/borge/anaconda3/lib/python3.7/json/decoder.py", line 337, in decode
        obj, end = self.raw_decode(s, idx=_w(s, 0).end())
      File "/home/borge/anaconda3/lib/python3.7/json/decoder.py", line 355, in raw_decode
        raise JSONDecodeError("Expecting value", s, err.value) from None
    json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

`$ /home/borge/anaconda3/bin/conda-env create -f /home/borge/ficl/environment.yml`

  environment variables:
                 CIO_TEST=<not set>
  CONDA_AUTO_UPDATE_CONDA=false
        CONDA_DEFAULT_ENV=base
                CONDA_EXE=/home/borge/anaconda3/bin/conda
             CONDA_PREFIX=/home/borge/anaconda3
    CONDA_PROMPT_MODIFIER=(base)
         CONDA_PYTHON_EXE=/home/borge/anaconda3/bin/python
               CONDA_ROOT=/home/borge/anaconda3
              CONDA_SHLVL=1
                     PATH=/home/borge/anaconda3/bin:/home/borge/.vscode-
                          server/bin/441438abd1ac652551dbe4d408dfcec8a499b8bf/bin/remote-cli:/ho
                          me/borge/.local/bin:/home/borge/anaconda3/bin:/home/borge/anaconda3/co
                          ndabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/u
                          sr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Windows/System32/HWA
                          udioDriverLibs:/mnt/c/Windows/system32:/mnt/c/Windows:/mnt/c/Windows/S
                          ystem32/Wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0:/mnt/c/Win
                          dows/System32/OpenSSH:/mnt/c/Users/Administrator/AppData/Local/Microso
                          ft/WindowsApps:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/S
                          ystem32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0:/mnt/c/WIN
                          DOWS/System32/OpenSSH:/mnt/c/Program Files/Git/cmd:/mnt/c/Users/georg/
                          AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/georg/AppData/Local/G
                          itHubDesktop/bin:/mnt/c/Users/georg/AppData/Local/Programs/Microsoft
                          VS Code/bin:/snap/bin
       REQUESTS_CA_BUNDLE=<not set>
            SSL_CERT_FILE=<not set>

     active environment : base
    active env location : /home/borge/anaconda3
            shell level : 1
       user config file : /home/borge/.condarc
 populated config files : 
          conda version : 4.7.12
    conda-build version : 3.18.9
         python version : 3.7.4.final.0
       virtual packages : 
       base environment : /home/borge/anaconda3  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /home/borge/anaconda3/pkgs
                          /home/borge/.conda/pkgs
       envs directories : /home/borge/anaconda3/envs
                          /home/borge/.conda/envs
               platform : linux-64
             user-agent : conda/4.7.12 requests/2.22.0 CPython/3.7.4 Linux/5.15.79.1-microsoft-standard-WSL2 ubuntu/20.04.3 glibc/2.31
                UID:GID : 1000:1000
             netrc file : None
           offline mode : False


An unexpected error has occurred. Conda has prepared the above report.
```

says that it failed on the transaction

### thoughts from AI

The error message `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` indicates that there was an issue with trying to read a JSON file or string. Specifically, the error message suggests that the JSON parser expected to find a value (e.g. a string, number, boolean, null, or an object/array made up of these types) at the beginning of the file, but instead found no content at all (hence `column 1 (char 0)`).

In this case, the error occurred when running the `conda-env` command with the argument `create -f /home/borge/ficl/environment.yml`. This suggests that the `environment.yml` file is either empty or not a properly formatted YAML file. To resolve the issue, you should check the contents of `environment.yml` to ensure that it is a valid YAML file with the necessary information to create the environment.

- everything still runs though

- ![Pasted image 20230217171829.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217171829.png)
- Noticed that we are on a very old conda here so have updated conda
- returning:
- ![Pasted image 20230217171942.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217171942.png)
- going to try again and see what happens with new conda
- collecting packages again - done
- solving environment - taking ages - still taking ages - failed:
```

    Traceback (most recent call last):
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/exceptions.py", line 1074, in __call__
        return func(*args, **kwargs)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda_env/cli/main.py", line 78, in do_call
        exit_code = getattr(module, func_name)(args, parser)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda_env/cli/main_create.py", line 102, in execute
        result[installer_type] = installer.install(prefix, pkg_specs, args, env)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda_env/installers/conda.py", line 32, in install
        unlink_link_transaction.execute()
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 244, in execute
        self.verify()
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/common/io.py", line 88, in decorated
        return f(*args, **kwds)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 221, in verify
        self.prepare()
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 213, in prepare
        stp.neutered_specs)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 288, in _prepare
        for prec, pcrec in zip(link_precs, pkg_cache_recs_to_link))
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/core/link.py", line 288, in <genexpr>
        for prec, pcrec in zip(link_precs, pkg_cache_recs_to_link))
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/gateways/disk/read.py", line 100, in read_package_info
        paths_data = read_paths_json(epd)
      File "/home/borge/anaconda3/lib/python3.7/site-packages/conda/gateways/disk/read.py", line 170, in read_paths_json
        data = json.load(paths_json)
      File "/home/borge/anaconda3/lib/python3.7/json/__init__.py", line 296, in load
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
      File "/home/borge/anaconda3/lib/python3.7/json/__init__.py", line 348, in loads
        return _default_decoder.decode(s)
      File "/home/borge/anaconda3/lib/python3.7/json/decoder.py", line 337, in decode
        obj, end = self.raw_decode(s, idx=_w(s, 0).end())
      File "/home/borge/anaconda3/lib/python3.7/json/decoder.py", line 355, in raw_decode
        raise JSONDecodeError("Expecting value", s, err.value) from None
    json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

`$ /home/borge/anaconda3/bin/conda-env create -f /home/borge/ficl/environment.yml`

  environment variables:
                 CIO_TEST=<not set>
  CONDA_AUTO_UPDATE_CONDA=false
        CONDA_DEFAULT_ENV=base
                CONDA_EXE=/home/borge/anaconda3/bin/conda
             CONDA_PREFIX=/home/borge/anaconda3
    CONDA_PROMPT_MODIFIER=(base)
         CONDA_PYTHON_EXE=/home/borge/anaconda3/bin/python
               CONDA_ROOT=/home/borge/anaconda3
              CONDA_SHLVL=1
                     PATH=/home/borge/anaconda3/bin:/home/borge/.vscode-
                          server/bin/441438abd1ac652551dbe4d408dfcec8a499b8bf/bin/remote-cli:/ho
                          me/borge/.local/bin:/home/borge/anaconda3/bin:/home/borge/anaconda3/co
                          ndabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/u
                          sr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Windows/System32/HWA
                          udioDriverLibs:/mnt/c/Windows/system32:/mnt/c/Windows:/mnt/c/Windows/S
                          ystem32/Wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0:/mnt/c/Win
                          dows/System32/OpenSSH:/mnt/c/Users/Administrator/AppData/Local/Microso
                          ft/WindowsApps:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/S
                          ystem32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0:/mnt/c/WIN
                          DOWS/System32/OpenSSH:/mnt/c/Program Files/Git/cmd:/mnt/c/Users/georg/
                          AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/georg/AppData/Local/G
                          itHubDesktop/bin:/mnt/c/Users/georg/AppData/Local/Programs/Microsoft
                          VS Code/bin:/snap/bin
       REQUESTS_CA_BUNDLE=<not set>
            SSL_CERT_FILE=<not set>

     active environment : base
    active env location : /home/borge/anaconda3
            shell level : 1
       user config file : /home/borge/.condarc
 populated config files : 
          conda version : 4.7.12
    conda-build version : 3.18.9
         python version : 3.7.4.final.0
       virtual packages : 
       base environment : /home/borge/anaconda3  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /home/borge/anaconda3/pkgs
                          /home/borge/.conda/pkgs
       envs directories : /home/borge/anaconda3/envs
                          /home/borge/.conda/envs
               platform : linux-64
             user-agent : conda/4.7.12 requests/2.22.0 CPython/3.7.4 Linux/5.15.79.1-microsoft-standard-WSL2 ubuntu/20.04.3 glibc/2.31
                UID:GID : 1000:1000
             netrc file : None
           offline mode : False


An unexpected error has occurred. Conda has prepared the above report.
```
 
- failing on the same bit:

 ```linux
 raw_decode
        raise JSONDecodeError("Expecting value", s, err.value) from None
    json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
``` 
can't work out

- conda still seems to be on an old version running:
`conda update --all` ![Pasted image 20230217174712.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217174712.png)
![Pasted image 20230217174712.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217174712.png)
- ![Pasted image 20230217174639.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230217174639.png)

 
## Now will try uninstalling conda and installing the newest:

Asking AI:

To uninstall conda in Ubuntu WSL, you can follow these steps:

1.  First, open a terminal window in your Ubuntu WSL.
    
2.  If you have conda environment activated, deactivate it by running:
    
    
    `conda deactivate`
    
3.  Next, run the following command to remove the conda package:
    
    
    `sudo apt-get remove conda`
    
4.  Once the package is removed, you can also remove the conda environment by running the following command:
    
    
    `rm -rf ~/anaconda3`
    
    This command assumes that your conda environment is installed in the default location. If you have installed it in a different location, you should update the path accordingly.
    
5.  Finally, remove the conda entry from your PATH environment variable by editing the `.bashrc` file:
    
    
    `nano ~/.bashrc`
    
    In the `.bashrc` file, look for any lines that add the conda installation path to the PATH variable, and remove them.
    
6.  Save and exit the file by pressing `Ctrl+X`, then `Y`, then `Enter`.
    
7.  Restart your terminal or run the following command to apply the changes to your current terminal session:
    
    
    `source ~/.bashrc`
    

After following these steps, conda should be completely uninstalled from your Ubuntu WSL.



## 2023-02-20

uninstalling current conda and going to install the most recent

ran:
`conda deactivate`

ran:
`sudo apt-get remove conda`
returned:
![Pasted image 20230220131103.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220131103.png)
says it cannot find conda but i feel that is probably good right?
not sure

ran: 
`rm -rf ~/anaconda3`

ran:
`nano ~/.bashrc`

opened a menu but could not find the bash files:

ran:
`conda --version`
returned:
![Pasted image 20230220131419.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220131419.png)


- running  `ls -l` in home directory reveals conda file structure is gone but the original install is still there
- will remove using  `rm Anaconda3-2019.10-Linux-x86_64.sh`
- returning:
- ![Pasted image 20230220131756.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220131756.png)
- successful
- have downloaded the newest version of conda  for linux from website
- Will add the file to the home directory
- ![Pasted image 20230220131948.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220131948.png)
- decided to remove the zone identifier as it says that it is a metadata file created by windows for downloaded files
- ![Pasted image 20230220132443.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220132443.png)
- adding write privalleges to the new conda file:
- ![Pasted image 20230220132637.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220132637.png)
- executing the conda file:
- ![Pasted image 20230220132750.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220132750.png)
- ![Pasted image 20230220132923.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220132923.png)
- cannot find anaconda in borge it appears it has gone in root
- dad reckons that i could modify the path but it will be easier just to install it in borge
- ![Pasted image 20230220134148.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220134148.png)
- wooooooo finally lmao
- now seek to run the environment file in the terminal in VS-code
- ![Pasted image 20230220134622.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220134622.png)
- installing loadsssss of packages lol
- ![Pasted image 20230220135156.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220135156.png)
- fookin success
- now will activate environment
- ![Pasted image 20230220135545.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220135545.png)
- success
- now will try running the test data
- ![Pasted image 20230220141715.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220141715.png)
- wasn't working for ages but noticed needed to be in the ficl directory and then it worked
- ran pytest and got big error like steven said
- ![Pasted image 20230220143444.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220143444.png)
- error comes from ficl not seeing gax like steven said so need to install gax with pip:


- installed gax using pip by:
```run-python
(ficl) borge@Borge:~/gax/gax$ python setup.py sdist
running sdist
running egg_info
creating gax.egg-info
writing gax.egg-info/PKG-INFO
writing dependency_links to gax.egg-info/dependency_links.txt
writing top-level names to gax.egg-info/top_level.txt
writing manifest file 'gax.egg-info/SOURCES.txt'
reading manifest file 'gax.egg-info/SOURCES.txt'
writing manifest file 'gax.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt, README.md

running check
creating gax-1
creating gax-1/gax.egg-info
creating gax-1/test
copying files to gax-1...
copying setup.py -> gax-1
copying gax.egg-info/PKG-INFO -> gax-1/gax.egg-info
copying gax.egg-info/SOURCES.txt -> gax-1/gax.egg-info
copying gax.egg-info/dependency_links.txt -> gax-1/gax.egg-info
copying gax.egg-info/top_level.txt -> gax-1/gax.egg-info
copying test/__init__.py -> gax-1/test
copying test/test_fftconvolve.py -> gax-1/test
copying test/test_sersic.py -> gax-1/test
copying test/test_sersic_bn.py -> gax-1/test
copying test/utilities.py -> gax-1/test
Writing gax-1/setup.cfg
creating dist
Creating tar archive
removing 'gax-1' (and everything under it)
(ficl) borge@Borge:~/gax/gax$ ls -l
total 68
-rw-r--r-- 1 borge borge   271 Feb 16 18:26 __init__.py
drwxr-xr-x 2 borge borge  4096 Feb 17 18:17 __pycache__
drwxr-xr-x 2 borge borge  4096 Feb 20 15:07 dist
-rw-r--r-- 1 borge borge  4351 Feb 16 18:26 fftconvolve.py
drwxr-xr-x 2 borge borge  4096 Feb 20 15:07 gax.egg-info
-rw-r--r-- 1 borge borge  2521 Feb 17 18:17 gax_fits.py
-rw-r--r-- 1 borge borge 14736 Feb 16 18:26 integration.py
-rw-r--r-- 1 borge borge  4523 Feb 16 18:26 model.py
-rw-r--r-- 1 borge borge  6135 Feb 16 18:26 sersic.py
-rw-r--r-- 1 borge borge   188 Feb 20 15:07 setup.py
drwxr-xr-x 2 borge borge  4096 Feb 16 18:26 test
(ficl) borge@Borge:~/gax/gax$ pip install /home/borge/gax/gax/dist/gax-1.tar.gz
Processing ./dist/gax-1.tar.gz
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: gax
  Building wheel for gax (setup.py) ... done
  Created wheel for gax: filename=gax-1-py3-none-any.whl size=7024 sha256=0e64e4eb8eaa8bb8079f80bd202d2c7b26b00f460d1ddf6374c2a861e53eb5dc
  Stored in directory: /home/borge/.cache/pip/wheels/b9/d8/47/bba8b2f9860d05f3a3545b76ed41bd03bf606b56664b5e18f4
Successfully built gax
Installing collected packages: gax
Successfully installed gax-1
(ficl) borge@Borge:~/gax/gax$ 
```


- This turned out to be wrong and so instead emailed stevebn and he sadi create the gax package with:
`pip install -e .` in the gax folder

- This worked
- After running the pytests and then the ficl code on the test data have viewed the resulting fits 
- ![Pasted image 20230220183632.png](../../../AA%20%20-%20%20Assets/Pasted%20image%2020230220183632.png) figure of residuals after 171 iterations in testing notebook

- files in the testing notebook [Borge_test.ipynb](../Code%20description/Juptyer%20Notebooks/Borge_test.ipynb.md) - the program has created 171 sets of 5 fits files so need to clean this up soon
- have deleted the iterations folder but saved the final results into the the self made data folder

# Now want to run ficl on a spiral galaxy image

- Setting up command: 

`python -m ficl.main --image_filename /home/borge/ficl/ficl/test/data/test_image.fits --output_path /home/borge/Data --max_iterations 60 --save_iteration_frequency 20 --modeller gax` 

`python -m ficl.main --image_filename /home/borge/ficl/ficl/test/data/587722981742149718ga.fits.gz --max_iterations 60 --save_iteration_frequency 20 `

# scipy.interpolate.interp1d

_class_ scipy.interpolate.interp1d(_x_, _y_, _kind='linear'_, _axis=-1_, _copy=True_, _bounds_error=None_, _fill_value=nan_, _assume_sorted=False_)[source](source.md)(https://github.com/scipy/scipy/blob/v1.10.1/scipy/interpolate/_interpolate.py#L385-L792)[](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d "Permalink to this definition")

Interpolate a 1-D function.

_x_ and _y_ are arrays of values used to approximate some function f: `y = f(x)`. This class returns a function whose call method uses interpolation to find the value of new points.

Parameters:

**x**(N,) array_like

A 1-D array of real values.

**y**(…,N,…) array_like

A N-D array of real values. The length of _y_ along the interpolation axis must be equal to the length of _x_.

**kind**str or int, optional

Specifies the kind of interpolation as a string or as an integer specifying the order of the spline interpolator to use. The string has to be one of ‘linear’, ‘nearest’, ‘nearest-up’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘previous’, or ‘next’. ‘zero’, ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of zeroth, first, second or third order; ‘previous’ and ‘next’ simply return the previous or next value of the point; ‘nearest-up’ and ‘nearest’ differ when interpolating half-integers (e.g. 0.5, 1.5) in that ‘nearest-up’ rounds up and ‘nearest’ rounds down. Default is ‘linear’.

**axis**int, optional

Specifies the axis of _y_ along which to interpolate. Interpolation defaults to the last axis of _y_.

**copy**bool, optional

If True, the class makes internal copies of x and y. If False, references to _x_ and _y_ are used. The default is to copy.

**bounds_error**bool, optional

If True, a ValueError is raised any time interpolation is attempted on a value outside of the range of x (where extrapolation is necessary). If False, out of bounds values are assigned [`fill_value`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.fill_value.html#scipy.interpolate.interp1d.fill_value "scipy.interpolate.interp1d.fill_value"). By default, an error is raised unless `fill_value="extrapolate"`.

**fill_value**array-like or (array-like, array_like) or “extrapolate”, optional

-   if a ndarray (or float), this value will be used to fill in for requested points outside of the data range. If not provided, then the default is NaN. The array-like must broadcast properly to the dimensions of the non-interpolation axes.
    
-   If a two-element tuple, then the first element is used as a fill value for `x_new < x[0]` and the second element is used for `x_new > x[-1]`. Anything that is not a 2-element tuple (e.g., list or ndarray, regardless of shape) is taken to be a single array-like argument meant to be used for both bounds as `below, above = fill_value, fill_value`. Using a two-element tuple or ndarray requires `bounds_error=False`.
    
    New in version 0.17.0.
    
-   If “extrapolate”, then points outside the data range will be extrapolated.
    
    New in version 0.17.0.
    

**assume_sorted**bool, optional

If False, values of _x_ can be in any order and they are sorted first. If True, _x_ has to be an array of monotonically increasing values.

See also

[`splrep`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splrep.html#scipy.interpolate.splrep "scipy.interpolate.splrep"), [`splev`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splev.html#scipy.interpolate.splev "scipy.interpolate.splev")

Spline interpolation/smoothing based on FITPACK.

[`UnivariateSpline`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html#scipy.interpolate.UnivariateSpline "scipy.interpolate.UnivariateSpline")

An object-oriented wrapper of the FITPACK routines.

[`interp2d`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp2d.html#scipy.interpolate.interp2d "scipy.interpolate.interp2d")

2-D interpolation

Notes

Calling [`interp1d`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d "scipy.interpolate.interp1d") with NaNs present in input values results in undefined behaviour.

Input values _x_ and _y_ must be convertible to _float_ values like _int_ or _float_.

If the values in _x_ are not unique, the resulting behavior is undefined and specific to the choice of _kind_, i.e., changing _kind_ will change the behavior for duplicates.

Examples

>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> from scipy import interpolate
>>> x = np.arange(0, 10)
>>> y = np.exp(-x/3.0)
>>> f = interpolate.interp1d(x, y)

>>> xnew = np.arange(0, 9, 0.1)
>>> ynew = f(xnew)   # use interpolation function returned by `interp1d`
>>> plt.plot(x, y, 'o', xnew, ynew, '-')
>>> plt.show()