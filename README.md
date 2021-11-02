# python-automation
python automated processing script, including web, excel, pdf, word, email, etc.

* [web]([python自动化-从web获取信息 - tensor_zhang - 博客园 (cnblogs.com)](https://www.cnblogs.com/tensorzhang/p/15449084.html#2048自动玩游戏))

  * [searchResultsOpener.py](https://github.com/MrZhangKY/python-automation/blob/main/web/searchResultsOpener.py): a script that can automatically use bing to search and open the first ten links.

    ```cmd
    python searchResultsOpener.py searchContent
    ```

  * [downloadXkcd.py](https://github.com/MrZhangKY/python-automation/blob/main/web/downloadXkcd.py): a script that can automatically download comic from XKCD.

    ```cmd
    python downloadXkcd.py
    ```

  * [163EmailSender.py-unfinished](https://github.com/MrZhangKY/python-automation/blob/main/web/163EmailSender.py):a script that can automatically log into the mailbox of 163 and send the specified mail to the specified mailbox.

    ```cmd
    python 163EmailSender.py mailAddress passWord  specifiedMailbox specifiedMail
    ```

    * Currently, only the automatic login function is completed, and automatic authentication is not available.

  * [2048player.py](https://github.com/MrZhangKY/python-automation/blob/main/web/2048player.py): a script that can open online 2048 game, automatically play games, get scores and board state, and automatically restart after deatch.

    ```cmd
    python 2048player.py
    ```

    * Currently, there is a lack of intelligent decision making module that can help automatically play games to get higher score. 

