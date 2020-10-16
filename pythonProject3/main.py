
"""
In this exercise you will use regex in order to make manipulations on patterns in strings
"""
# import regex here:
import re
def bunny():
    messy_text = """This http://www.foo.com/gag.txt is a web URL. This other one HTTP://WWW.UPPERCASE.COM is too.
    on the other hand httl://www.google.com/index.html and mailto:fooman@foo.com are not.
    http://spaz.info/31415.html is quite OK too. http:///www.cnn.com is messed up."""

    # Use findall function to extract all the valid urls from the messy text. Beware not to get an e-mail in your list.
    check = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|HTTP[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    print(check.findall(messy_text))

    #Here is a potential animal:
    potential_animal = """0000zzzVVVzzzWWWzzzVVV---_WWW......._-_--.
    WWWWWWzzzWWW[a(>RWWW$0000aaaazzz$zzz$>VVVR0000WWW@
    0000aaWWWVVV0000$aWWWx[[[zzzzzz.'aa-=-'aWWWVVV`.
    WWW[[aWWWxzzzzzzx00000000aa.'VVVzzzVVVVVVzzzzzzWWWVVVzzzWWWzzzVVVVVV)
    0000VVV0000_xVVV[xzzzWWWa.'00000000VVV0000[aazzz_.)0000zzz0000$
    0000a$WWWoWWW[WWWozzzaazzz[0000[zzz_.-'VVVxWWW0000.'
    0000zzzRa0000a0000zzzzzz0000VVVWWWa_.-'VVVazzzax0000.'*2
    VVVVVVVVVR______.-'xxVVVWWW0000WWW.'.'zzzR*>
    VVVWWW0000a@2zzzVVV@VVV>zzzx$VVVzzzWWW.'.'WWW_WWW>*2
    VVV[0000[zzz`[VVVa@>$$zzza.'.'_a_[_>*>
    WWW0000VVVVVVVVVWWW.aa.$x[.'.'WWW2zzz_0000_WWW@*>
    [0000[zzzzzzWWWR`-2R_$zzzx0000VVVaWWW@a_[_a@*@
    00000000[zzz[WWWa`$'@__x[0000WWW0000VVVzzz@VVV_[_[R*@
    WWWa[zzzaVVV$^2azzzzzzzzz[0000VVVVVVVVVWWWVVVaR0000_a_aR*
    zzzWWWzzzzzzWWW'zzzWWW`[zzz[zzzaVVVa0000VVVWWWWWWzzzaR0000_[_a@
    ASHa(+VK)zzzWWWVVV[WWW0000[[[00000000zzzWWWa@_"""

    real_animal = potential_animal
    #here is one substitution that you will need
    real_bunny = re.sub(r"a|VVV|zzz|0000|\[|WWW", r" ", real_animal)
    # replace all instances of x and $ with / here:
    real_bunny = re.sub(r"x|\$", r"/", real_bunny)
    # replace all insances of @ and R with \ here:
    real_bunny = re.sub(r"@|R", r"\\", real_bunny)
    # replace all instances of > and 2 with | here:
    real_bunny = re.sub(r">|2", r"|", real_bunny)

    with open("my_regex_animal.txt", "a") as f:
        f.write("\n" + real_bunny)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bunny()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
