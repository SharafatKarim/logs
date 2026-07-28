# Flutter without android studio

Setting up Flutter and the Android SDK on Arch Linux without the heavy Android Studio IDE is highly efficient and keeps your system lean. We will use the official Android Command Line Tools and install Flutter manually to avoid permission issues that can sometimes happen with AUR packages.

Here is how to set up your environment from scratch.

1. **Install Prerequisites:** Java, Git, and Arch utilities.
Flutter and Android both rely on Java. While Arch often provides the latest Java versions, Java 17 is currently the most stable choice for Android development. You also need standard build and extraction tools.

Open your terminal and run:

```bash
sudo pacman -S base-devel git unzip wget jdk17-openjdk android-udev

```

*(Note: `android-udev` helps your system recognize physical Android devices when plugged in via USB).*

2. **Set Up the Android SDK Directory:**
The Android SDK expects a very specific folder structure to work properly. Let's create the base folder and the specific path where the command-line tools will live.

```bash
mkdir -p ~/Android/Sdk/cmdline-tools
cd ~/Android/Sdk/cmdline-tools

```

3. **Download the Android Command Line Tools:**
Instead of Android Studio, we will download Google's bare-metal CLI tools.

- Go to the [Android Studio Downloads page](https://developer.android.com/studio#command-tools) in your browser.
- Scroll down to the **Command line tools only** section.
- Download the `.zip` file for **Linux**.
- Move the downloaded zip file to the folder you just created (`~/Android/Sdk/cmdline-tools/`) and extract it.

**Crucial renaming step:** The extracted folder will be named `cmdline-tools`. You *must* rename it to `latest` for the SDK manager to recognize it properly.

```bash
# Assuming you downloaded it to ~/Downloads
mv ~/Downloads/commandlinetools-linux-*_latest.zip ~/Android/Sdk/cmdline-tools/
unzip commandlinetools-linux-*_latest.zip
mv cmdline-tools latest
rm commandlinetools-linux-*_latest.zip

```

4. **Download Flutter SDK:** Via Git.
Next, let's grab the Flutter SDK directly from its stable GitHub branch. Placing it in a `~/development` folder is standard practice.

```bash
mkdir -p ~/development
cd ~/development
git clone https://github.com/flutter/flutter.git -b stable

```

5. **Configure Environment Variables:**
You need to tell your shell where to find these new tools. Open your shell configuration file (usually `~/.bashrc` or `~/.zshrc`) in your preferred text editor:

```bash
nano ~/.bashrc

```

Add the following lines to the very bottom of the file:

```bash
# Android Setup
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/emulator

# Flutter Setup
export PATH=$PATH:$HOME/development/flutter/bin

```

Save and exit, then reload your shell configuration so the changes take effect:

```bash
source ~/.bashrc

```

6. **Install the required SDK and Build Tools:**
Run the `sdkmanager` command to download SDK 36 and the specific build tools Flutter is missing. It is best to grab both the API 36 build tools and the legacy 28.0.3 version it complains about.

```bash
sdkmanager "platforms;android-36" "build-tools;36.0.0" "build-tools;28.0.3"

```

Once the download finishes, you must accept the Android licenses. Run this command and press `y` for each prompt:

```bash
sdkmanager --licenses

```

7. **Accept the new licenses:**
Whenever you download new SDK components, you must agree to the associated Google licenses.

```bash
flutter doctor --android-licenses

```

Press `y` to accept any unapproved licenses.

8. **Verify the fix:**
Run the doctor command again to confirm the Android toolchain is fully resolved.

```bash
flutter doctor

```
