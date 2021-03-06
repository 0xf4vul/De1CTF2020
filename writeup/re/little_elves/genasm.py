#!/usr/bin/python3
# python3 genasm.py > little_elves.asm && nasm -f bin -o little_elves little_elves.asm
# 
import random
A = [[166, 8, 116, 187, 48, 79, 49, 143, 88, 194, 27, 131, 58, 75, 251, 195, 192, 185, 69, 60, 84, 24, 124, 33, 211, 251, 140, 124, 161, 9, 44, 208, 20, 42, 8, 37, 59, 147, 79, 232, 57, 16, 12, 84], [73, 252, 81, 126, 50, 87, 184, 130, 196, 114, 29, 107, 153, 91, 63, 217, 31, 191, 74, 176, 208, 252, 97, 253, 55, 231, 82, 169, 185, 236, 171, 86, 208, 154, 192, 109, 255, 62, 35, 140, 91, 49, 139, 255], [57, 18, 43, 102, 96, 26, 50, 187, 129, 161, 7, 55, 11, 29, 151, 219, 203, 139, 56, 12, 176, 160, 250, 237, 1, 238, 239, 211, 241, 254, 18, 13, 75, 47, 215, 168, 149, 154, 33, 222, 77, 138, 240, 42], [96, 198, 230, 11, 49, 62, 42, 10, 169, 77, 7, 164, 198, 241, 131, 157, 75, 147, 201, 103, 120, 133, 161, 14, 214, 157, 28, 220, 165, 232, 20, 132, 16, 79, 9, 1, 33, 194, 192, 55, 109, 166, 101, 110], [108, 159, 167, 183, 165, 180, 74, 194, 149, 63, 211, 153, 174, 97, 102, 123, 157, 142, 47, 30, 185, 209, 57, 108, 170, 161, 126, 248, 206, 238, 140, 105, 192, 231, 237, 36, 46, 185, 123, 161, 97, 192, 168, 129], [72, 18, 132, 37, 37, 42, 224, 99, 92, 159, 95, 27, 18, 172, 43, 251, 97, 44, 238, 106, 42, 86, 124, 1, 231, 63, 99, 147, 239, 180, 217, 195, 203, 106, 21, 4, 238, 229, 43, 232, 193, 31, 116, 213], [17, 133, 116, 7, 57, 79, 20, 19, 197, 146, 5, 40, 103, 56, 135, 185, 168, 73, 3, 113, 118, 102, 210, 99, 29, 12, 34, 249, 237, 132, 57, 71, 44, 41, 1, 65, 136, 112, 20, 142, 162, 232, 225, 15], [224, 192, 5, 102, 220, 42, 18, 221, 124, 173, 85, 87, 112, 175, 157, 72, 160, 207, 229, 35, 136, 157, 229, 10, 96, 186, 112, 156, 69, 195, 89, 86, 238, 167, 169, 154, 137, 47, 205, 238, 22, 49, 177, 83], [234, 233, 189, 191, 209, 106, 254, 220, 45, 12, 242, 132, 93, 12, 226, 51, 209, 114, 131, 4, 51, 119, 117, 247, 19, 219, 231, 136, 251, 143, 203, 145, 203, 212, 71, 210, 12, 255, 43, 189, 148, 233, 199, 224], [5, 62, 126, 209, 242, 136, 95, 189, 79, 203, 244, 196, 2, 251, 150, 35, 182, 115, 205, 78, 215, 183, 88, 246, 208, 211, 161, 35, 39, 198, 171, 152, 231, 57, 44, 91, 81, 58, 163, 230, 179, 149, 114, 105], [72, 169, 107, 116, 56, 205, 187, 117, 2, 157, 39, 28, 149, 94, 127, 255, 60, 45, 59, 254, 30, 144, 182, 156, 159, 26, 39, 44, 129, 34, 111, 174, 176, 230, 253, 24, 139, 178, 200, 87, 44, 71, 67, 67], [5, 98, 151, 83, 43, 8, 109, 58, 204, 250, 125, 152, 246, 203, 135, 195, 8, 164, 195, 69, 148, 14, 71, 94, 81, 37, 187, 64, 48, 50, 230, 165, 20, 167, 254, 153, 249, 73, 201, 40, 106, 3, 93, 178], [104, 212, 183, 194, 181, 196, 225, 130, 208, 159, 255, 32, 91, 59, 170, 44, 71, 34, 99, 157, 194, 182, 86, 167, 148, 206, 237, 196, 250, 113, 22, 244, 100, 185, 47, 250, 33, 253, 204, 44, 191, 50, 146, 181], [143, 5, 236, 210, 136, 80, 252, 104, 156, 100, 209, 109, 103, 134, 125, 138, 115, 215, 108, 155, 191, 160, 228, 183, 21, 157, 225, 61, 89, 198, 250, 57, 189, 89, 205, 152, 184, 86, 207, 72, 65, 20, 209, 155], [103, 51, 118, 167, 111, 152, 184, 97, 213, 190, 175, 93, 237, 141, 92, 30, 82, 136, 16, 212, 99, 21, 105, 166, 161, 214, 103, 21, 116, 161, 148, 132, 95, 54, 60, 161, 207, 183, 250, 45, 156, 81, 208, 15], [150, 65, 4, 37, 202, 4, 54, 106, 113, 55, 51, 181, 225, 120, 173, 61, 251, 42, 153, 149, 88, 160, 79, 197, 204, 20, 65, 79, 165, 85, 203, 193, 203, 97, 9, 142, 53, 50, 127, 193, 225, 11, 121, 148], [99, 27, 20, 52, 248, 197, 117, 210, 216, 249, 122, 48, 225, 117, 211, 2, 33, 172, 60, 140, 84, 44, 71, 187, 160, 198, 26, 100, 162, 92, 89, 181, 82, 55, 184, 152, 112, 51, 248, 255, 205, 145, 31, 137], [209, 78, 219, 94, 189, 146, 92, 172, 214, 106, 122, 121, 90, 60, 174, 6, 82, 28, 166, 206, 248, 86, 28, 113, 159, 183, 196, 12, 183, 146, 225, 107, 169, 128, 67, 221, 228, 244, 212, 66, 118, 136, 162, 218], [163, 143, 112, 123, 98, 87, 0, 143, 198, 176, 196, 246, 231, 201, 157, 169, 244, 123, 106, 210, 50, 159, 47, 55, 28, 203, 235, 91, 74, 16, 175, 125, 53, 54, 82, 2, 112, 159, 122, 251, 118, 138, 120, 184], [187, 81, 128, 55, 221, 223, 44, 37, 166, 168, 32, 169, 22, 255, 169, 251, 101, 158, 161, 153, 89, 1, 244, 87, 246, 237, 157, 232, 180, 3, 248, 23, 58, 162, 144, 159, 173, 28, 117, 196, 186, 225, 81, 83], [169, 45, 229, 173, 17, 248, 83, 201, 242, 38, 116, 201, 12, 87, 3, 231, 200, 143, 166, 63, 146, 86, 240, 197, 26, 198, 21, 34, 202, 192, 26, 188, 203, 3, 13, 238, 109, 179, 214, 146, 193, 255, 226, 189], [16, 63, 38, 178, 184, 25, 51, 81, 142, 189, 2, 37, 163, 244, 157, 193, 149, 21, 6, 215, 185, 13, 205, 56, 158, 45, 48, 243, 98, 248, 129, 223, 68, 111, 88, 62, 119, 28, 255, 243, 132, 238, 149, 75], [185, 141, 49, 173, 86, 9, 150, 99, 183, 114, 226, 133, 170, 2, 65, 124, 2, 164, 2, 155, 153, 89, 109, 220, 138, 127, 150, 213, 114, 6, 151, 227, 248, 172, 28, 0, 92, 63, 41, 229, 214, 120, 49, 164], [242, 48, 147, 252, 204, 89, 111, 168, 251, 136, 160, 106, 5, 155, 137, 198, 250, 250, 57, 180, 252, 118, 165, 21, 254, 155, 154, 247, 242, 217, 131, 65, 35, 207, 112, 77, 209, 176, 122, 192, 147, 107, 80, 37], [52, 183, 251, 29, 226, 175, 39, 75, 34, 254, 233, 96, 155, 144, 9, 254, 189, 41, 169, 184, 91, 97, 87, 88, 251, 138, 114, 118, 91, 156, 198, 75, 222, 19, 183, 52, 81, 194, 144, 13, 249, 111, 3, 73], [21, 107, 222, 106, 222, 98, 190, 4, 244, 225, 112, 133, 120, 253, 141, 48, 52, 154, 63, 235, 190, 78, 33, 209, 4, 172, 158, 187, 219, 151, 17, 233, 214, 32, 120, 38, 26, 0, 250, 129, 251, 40, 89, 39], [25, 66, 117, 107, 200, 80, 88, 90, 24, 176, 247, 95, 59, 121, 118, 67, 56, 133, 145, 167, 24, 46, 180, 145, 128, 220, 200, 29, 172, 157, 100, 9, 97, 253, 8, 200, 52, 229, 147, 218, 254, 255, 182, 170], [172, 79, 214, 26, 85, 230, 228, 223, 32, 227, 84, 74, 109, 209, 222, 45, 48, 66, 23, 197, 52, 212, 179, 184, 90, 149, 199, 128, 153, 70, 3, 73, 160, 39, 49, 165, 88, 252, 135, 9, 157, 140, 32, 33], [72, 233, 196, 173, 35, 166, 146, 186, 61, 86, 64, 42, 25, 86, 66, 93, 12, 255, 63, 83, 95, 219, 108, 152, 205, 31, 238, 77, 74, 156, 149, 228, 68, 244, 178, 78, 181, 173, 251, 248, 185, 99, 181, 205], [106, 86, 224, 51, 91, 194, 158, 83, 144, 77, 217, 95, 125, 119, 144, 47, 85, 220, 24, 40, 59, 77, 70, 190, 188, 20, 105, 150, 79, 85, 194, 168, 64, 215, 234, 226, 4, 99, 157, 0, 186, 74, 18, 94], [36, 23, 51, 78, 191, 254, 1, 166, 174, 62, 222, 243, 131, 207, 37, 4, 199, 35, 169, 7, 216, 42, 190, 241, 120, 11, 166, 129, 117, 93, 184, 50, 237, 84, 122, 67, 250, 248, 60, 96, 117, 91, 187, 79], [248, 17, 173, 127, 98, 184, 11, 20, 50, 140, 249, 248, 24, 222, 34, 86, 71, 0, 237, 138, 148, 107, 115, 104, 62, 191, 39, 221, 123, 115, 131, 229, 127, 56, 64, 177, 106, 239, 26, 255, 100, 88, 1, 75], [144, 18, 85, 103, 3, 31, 157, 44, 67, 24, 228, 226, 82, 208, 69, 17, 189, 216, 205, 140, 6, 1, 33, 11, 61, 223, 12, 116, 123, 167, 151, 58, 167, 79, 96, 189, 151, 233, 92, 94, 22, 60, 254, 254], [216, 167, 82, 244, 143, 231, 192, 63, 79, 49, 131, 176, 212, 46, 141, 107, 125, 207, 201, 5, 103, 155, 107, 166, 210, 49, 182, 60, 34, 26, 220, 198, 225, 160, 57, 52, 138, 27, 247, 181, 0, 67, 1, 205], [19, 243, 215, 203, 156, 157, 71, 187, 142, 198, 244, 52, 100, 195, 129, 134, 38, 227, 155, 241, 122, 192, 145, 179, 195, 16, 180, 70, 86, 219, 250, 67, 127, 47, 178, 249, 19, 36, 183, 50, 154, 186, 239, 15], [163, 224, 95, 10, 171, 106, 49, 57, 28, 178, 119, 6, 40, 228, 92, 163, 93, 225, 23, 37, 24, 211, 72, 105, 209, 70, 0, 165, 70, 226, 43, 187, 167, 60, 143, 233, 207, 209, 12, 207, 64, 246, 222, 16], [245, 140, 237, 250, 89, 99, 215, 112, 85, 182, 51, 26, 62, 220, 116, 17, 196, 247, 172, 121, 22, 106, 91, 200, 115, 240, 31, 78, 47, 126, 50, 114, 109, 88, 83, 120, 17, 95, 198, 206, 71, 112, 172, 49], [254, 198, 189, 175, 121, 123, 248, 38, 163, 170, 91, 171, 125, 66, 94, 37, 181, 207, 13, 60, 210, 178, 252, 39, 175, 18, 106, 94, 171, 196, 182, 129, 101, 165, 103, 164, 234, 110, 146, 69, 36, 75, 58, 98], [184, 162, 160, 24, 71, 214, 24, 14, 196, 222, 67, 178, 163, 150, 206, 104, 38, 176, 245, 98, 180, 213, 93, 134, 25, 198, 166, 10, 183, 99, 207, 127, 163, 10, 141, 105, 52, 68, 18, 121, 217, 209, 124, 127], [142, 153, 245, 130, 182, 55, 211, 250, 217, 10, 172, 119, 212, 171, 244, 99, 99, 41, 223, 221, 128, 66, 31, 129, 195, 145, 241, 50, 77, 139, 29, 232, 60, 167, 110, 139, 124, 135, 18, 197, 200, 85, 15, 159], [225, 159, 86, 55, 158, 137, 229, 250, 129, 194, 200, 31, 147, 30, 219, 233, 147, 28, 6, 219, 81, 172, 132, 162, 212, 115, 232, 60, 152, 105, 146, 77, 187, 9, 20, 191, 157, 96, 131, 190, 125, 175, 141, 4], [110, 75, 232, 58, 102, 13, 222, 137, 137, 14, 191, 155, 48, 100, 169, 184, 49, 249, 49, 39, 138, 124, 63, 73, 237, 150, 244, 126, 127, 206, 91, 252, 110, 45, 189, 116, 188, 42, 18, 68, 194, 244, 53, 2], [109, 116, 87, 241, 128, 121, 227, 188, 2, 6, 81, 194, 4, 225, 176, 48, 8, 59, 243, 50, 234, 228, 192, 176, 168, 187, 248, 244, 27, 188, 107, 204, 222, 202, 73, 141, 160, 139, 151, 206, 1, 227, 152, 81], [13, 149, 85, 158, 164, 119, 149, 36, 138, 84, 173, 132, 39, 230, 96, 229, 84, 218, 14, 153, 184, 98, 160, 129, 2, 161, 99, 41, 17, 114, 55, 67, 192, 102, 241, 168, 149, 191, 216, 18, 229, 153, 94, 171]]
res = [200, 201, 204, 116, 124, 94, 129, 127, 211, 85, 61, 154, 50, 51, 27, 28, 19, 134, 121, 70, 100, 219, 1, 132, 93, 252, 152, 87, 32, 171, 228, 156, 43, 98, 203, 2, 24, 63, 215, 186, 201, 128, 103, 52]
code_start = """BITS 32
            org     0x00888000
            db      0x7F, "ELF"             ; e_ident
            dd      1                                       ; p_type
            dd      0                                       ; p_offset
            dd      $$                                      ; p_vaddr 
            dw      2                       ; e_type        ; p_paddr
            dw      3                       ; e_machine
            dd      _start                  ; e_version     ; p_filesz
            dd      _start                  ; e_entry       ; p_memsz
            dd      4                       ; e_phoff       ; p_flags
_start:
            jmp     __start                 ; e_shoff       ; p_align
            db      0E8h
            dd      0DEADBEEFh
            db      0
            dw      0x34                    ; e_ehsize
            dw      0x20                    ; e_phentsize
            dw      1                       ; e_phnum
            dw      0                       ; e_shentsize
            dw      0                       ; e_shnum
            dw      0                       ; e_shstrndx
__start:
            lea     esp, [esp-45]
            mov     eax, 3
            xor     ebx, ebx
            lea     ecx, [esp]
            mov     edx, 45
            int     0x80
            xor     eax, eax
            call    loop00"""
code = """
loop%02d:     add     esp, 4
%s
loop_body%02d:mov     cl, byte [esp+edi]
            mov     dl, byte [mA%02d+edi]
            xor     esi, esi
loop_Gmul%02d:test    edx, 1
            jz      next0_%02d
            xor     ebx, ecx
next0_%02d:   test    ecx, 80h
            jz      next1_%02d
            shl     cl, 1
            xor     cl, 39h
            jmp     next2_%02d
next1_%02d:   shl     cl, 1
next2_%02d:   shr     dl, 1
            inc     esi
            cmp     esi, 8
            jnz     loop_Gmul%02d
            inc     edi
            cmp     edi, 44
            jnz     loop_body%02d
            cmp     ebx, %d
            setnz   bl
            or      eax, ebx
            call    loop%02d
mA%02d:       db      %s"""
code_end = """
loop44:     add     esp, 4
            mov     ebx, eax
            xor     eax, eax
            inc     eax
            int     0x80"""
def get_junk():
    res = "db      "
    t = random.randint(0,3)
    if t==0:
        res += "232"
        for i in range(random.randint(0,3)):
            res += ", " + str(random.randint(0, 255))
    elif t==1:
        res += "233"
        for i in range(random.randint(0,3)):
            res += ", " + str(random.randint(0, 255))
    elif t==2:
        res += "234"
        for i in range(random.randint(0,5)):
            res += ", " + str(random.randint(0, 255))
    else:
        res += "235"
    return res

res_code = code_start
for i in range(44):
    junkcode = """            xor     ecx, ecx
            jz      junk0_%02d
            %s
junk0_%02d:   xor     edi, edi
            jz      junk1_%02d
            %s
junk1_%02d:   xor     ebx, ebx
            jz      junk2_%02d
            %s
junk2_%02d:"""%(i, get_junk(), i, i, get_junk(), i, i, get_junk(), i)
    tmp = ""
    for j in A[i][:-1]:
        tmp += str(j) + ", "
    tmp += str(A[i][-1])
    res_code += code%(i,junkcode,i,i,i,i,i,i,i,i,i,i,i,res[i],i+1,i,tmp)
res_code += code_end
print(res_code)