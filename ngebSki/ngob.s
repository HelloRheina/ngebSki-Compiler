	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 15
	.globl	_main                           ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:                               ## %entry
	subq	$72, %rsp
	.cfi_def_cfa_offset 80
	movl	$-10, 68(%rsp)
	movl	$20, 64(%rsp)
	movl	$30, 60(%rsp)
	movl	$40, 56(%rsp)
	movl	$50, 52(%rsp)
	movl	$60, 48(%rsp)
	movl	$58, 44(%rsp)
	movl	$-6040, 40(%rsp)                ## imm = 0xE868
	movl	$-230, 36(%rsp)
	movl	$60, 32(%rsp)
	movl	$650, 28(%rsp)                  ## imm = 0x28A
	movl	$46, 24(%rsp)
	movl	$-200, 20(%rsp)
	movl	$56, 16(%rsp)
	movl	$-1, 12(%rsp)
	movl	$-12380, 8(%rsp)                ## imm = 0xCFA4
	movl	$3600, 4(%rsp)                  ## imm = 0xE10
	leaq	_fstr_0(%rip), %rdi
	movl	$58, %esi
	xorl	%eax, %eax
	callq	_printf
	movl	40(%rsp), %esi
	leaq	_fstr_1(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	movl	36(%rsp), %esi
	leaq	_fstr_2(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	movl	32(%rsp), %esi
	leaq	_fstr_3(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	movl	28(%rsp), %esi
	leaq	_fstr_4(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	movl	24(%rsp), %esi
	leaq	_fstr_5(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	movl	20(%rsp), %esi
	leaq	_fstr_6(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	movl	16(%rsp), %esi
	leaq	_fstr_7(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	movl	12(%rsp), %esi
	leaq	_fstr_8(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	movl	8(%rsp), %esi
	leaq	_fstr_9(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	movl	4(%rsp), %esi
	leaq	_fstr_10(%rip), %rdi
	xorl	%eax, %eax
	callq	_printf
	addq	$72, %rsp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__const
_fstr_0:                                ## @fstr_0
	.asciz	"%i\n"

_fstr_1:                                ## @fstr_1
	.asciz	"%i\n"

_fstr_2:                                ## @fstr_2
	.asciz	"%i\n"

_fstr_3:                                ## @fstr_3
	.asciz	"%i\n"

_fstr_4:                                ## @fstr_4
	.asciz	"%i\n"

_fstr_5:                                ## @fstr_5
	.asciz	"%i\n"

_fstr_6:                                ## @fstr_6
	.asciz	"%i\n"

_fstr_7:                                ## @fstr_7
	.asciz	"%i\n"

_fstr_8:                                ## @fstr_8
	.asciz	"%i\n"

_fstr_9:                                ## @fstr_9
	.asciz	"%i\n"

_fstr_10:                               ## @fstr_10
	.asciz	"%i\n"

.subsections_via_symbols
