import sys

p = []
with file(sys.argv[1]) as f:
    for l in f:
        if "//" in l:
            l = l[:l.index("//")]
        if l.strip() == "":
            continue
        l = l.strip().split(" ")
        if len(l) == 1:
            p.append([l[0], ""])
        else:
            p.append([l[0], l[1]])

pc = 0
st = []
while pc < len(p):
    i = p[pc]
    if i[0] == "INT":
        st.append(int(i[1]))
        pc += 1
    elif i[0] == "ADD":
        rhs = st.pop()
        lhs = st.pop()
        st.append(lhs + rhs)
        pc += 1
    elif i[0] == "SUB":
        rhs = st.pop()
        lhs = st.pop()
        st.append(lhs - rhs)
        pc += 1
    elif i[0] == "SWAP":
        t1 = st.pop()
        t2 = st.pop()
        st.append(t1)
        st.append(t2)
        pc += 1
    elif i[0] == "DUP":
        st.append(st[-1])
        pc += 1
    elif i[0] == "POP":
        st.pop()
        pc += 1
    elif i[0] == "CALL":
        st.append(pc + 1)
        pc = int(i[1])
    elif i[0] == "RET":
        pc = st.pop()
    elif i[0] == "JGE":
        if st[-1] >= 0:
            pc = int(i[1])
        else:
            pc += 1
    elif i[0] == "JEQ":
        if st[-1] == 0:
            pc = int(i[1])
        else:
            pc += 1
    elif i[0] == "PRINT":
        print(st[-1])
        pc += 1
    elif i[0] == "EXIT":
        break
    else:
        print i
        raise "XXX"