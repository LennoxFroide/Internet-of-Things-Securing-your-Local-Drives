# Internet-of-Things-Securing-your-Local-Drives
Ever felt like you need to take back some control on how much of the data stored in your local devices is accessible to big corporations or device manufacturers? Well, this project aims to help with this issue by showing anyone how to create a new VHD (virtual hard disk) and secure it using encryption.

<h1>Step 1:CREATING A VHD</h1>
<ul>
<li>Most personal computers come with a C drive that's the system drive. Since it's the system drive it's not easy to encrypt but there are ways to create a secure drive for yourself. To do this  we need to create a new virtual hard  disk (VHD).
Techtarget.com defines a VHD as a disk image file format for storing the entire content of a computer's hard drive. We'll just call it our "new drive" from now on.<br></li>
<br><li>To create the new drive, we need to use the disk management system from out computer's control pannel. On the Window's search bar type the key word "Disk management." This query returns "Create and format disk partitions," as one
of the results and you should click onto this.</li><br>
<li>Click onto an unallocated disk space and once it's highlighted, on the main menu at the top of the window click on the "Action" button. This displays a drop down menu
with "Create and Attach Virtual Hard Disk" as one of the options, select this option. Another window will pop up where you can select the location of the new drive and also pick between VHD and VHDX. Selecting VHDX is the better option as it is 
more reliable and dynamically expands. Select VHDX and click ok then close the Disk Management window.</li><br>
<li>Reopen the Disk Management window and a new window called "Initialize Disk" will pop up which allows you to create a Master Boot Record for our new disk. Select MBR and click ok. The new disk will now show up with an MBR and the next step is to right clisk onto an
unallocated space. This prompts a menu to pop up with "New Simple Volume" as an option. Click this option which will open a "New Simple Volume Wizard" that you'll use to name the new disk,
select the amount of memory that's allocated to it and then format the disk.</li><br>
<li>Now you can close the Disk Management window. To see your new disk navigate to "This PC" and the disk should show up alongside other existing disks such as the "Windows C Drive." </li>
</ul>
<h1>Step 2:ENCRYPTION SOFTWARE</h1>
<ul>
<li> Now that we have our new drive, we need to put security measures in place to ensure that unauthorized people cannot access the data in our drive, to do this we need to use encryption. According to Techtarget.com, encryption is defined as
the method by which information is converted into secret code that hides the information's true meaning. The Sceience of encrypting and decrypting information is called <b>cryptography</strong></b>
<li>Fortunately for us, most Windows versions including Windows 10 and 11 support BitLocker encryption that comes with the operating system and a user can enable it at their liking. To make using BitLocker encryption even easier, there are GUIs
such as M3 BitLocker Loader that you can use to easily see the drives available on your computer and you get to lock them easily by simply clicking lock drive.</li><br>
<li>You can dowload M3 BitLocker Loader for Windows at this address: https://www.m3datarecovery.com/bitlocker-windows-home/ </li><br>
<li>Click on the "Try It For Free" button to download the BitLocker Loader and <strong>run</strong> it once the download is complete to install it. Once it's installed, M3 BitLocker Loader will allow you to see all 
the drives in your PC that you can create an encryption key for and lock them.</li><br>
<li>If you're using Mac or even Linux there are available versions for these operating systems too that you can find at this link: https://www.m3datarecovery.com/bitlocker/</li>

</ul>
<h1>Step 3:CREATING AN ENCRYPTION KEY/PASSWORD</h1>
<ul>
<li>A key component of safe guarding this new drive is to create a password/ encryption key that's impenetrable. With a lot of AI systems out there coupled with the wide range of personal information that is easily available online, cyber attackers can use the information
to crack passwords that we form when relying on our own memory and thinking patterns. Therefore, to create an impenetrable password, we're going to use a <strong>Python encryption key generator</strong>.</li><br>
<li>This Python code, which is available in this repository, takes in an input from the user which is the desired lenth of their encyption key and creates a strong password of any length that's a combination of digits,letters and special characters. This key is randomly generated which makes it harder to crack for any cyber attacker who is using pre-existing user information from the internet.</li>
</ul>
<br>
We're all set now, we have a new drive that's encrypted, with a randomly generated encyption key that's always going to be required to access the drive contents once the drive is locked. Take note that your encyption key must not be photographed or in the line of sight of any cameras since photograph data is easily accessible to online attackers. If your password is ever photographed or viewed by anyone else,
you need to generate a new key with the <strong>Python encryption key generator</strong> immediately.
