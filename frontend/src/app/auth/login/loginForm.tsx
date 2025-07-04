"use client";

import React from "react";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { PasswordInput } from "@/app/auth/_components/PasswordInput";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

const formSchema = z.object({
    email: z.string().email(),
    password: z.string(),
});

export const LoginForm = () => {
    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            email: "",
            password: "",
        },
        mode: "all",
    });

    function onSubmit(values: z.infer<typeof formSchema>) {
        console.log(values);
    }

    return (
        <Form {...form}>
            <form
                onSubmit={form.handleSubmit(onSubmit)}
                className="space-y-4"
            >
                <FormField
                    control={form.control}
                    name="email"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>
                                <span>
                                    Email<sup className="text-sm text-rose-800">*</sup>
                                </span>
                            </FormLabel>
                            <FormControl>
                                <Input
                                    placeholder=""
                                    {...field}
                                    tabIndex={1}
                                />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />
                <FormField
                    control={form.control}
                    name="password"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>
                                {" "}
                                <span>
                                    Password<sup className="text-sm text-rose-800">*</sup>
                                </span>
                            </FormLabel>
                            <FormControl>
                                <PasswordInput
                                    {...field}
                                    tabIndex={3}
                                />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />
                <p className="text-right">
                    <Link
                        href="/auth/forgot-password"
                        className="w-full text-right text-sm font-semibold"
                        prefetch={false}
                    >
                        Forgot Password?
                    </Link>
                </p>
                <Button
                    type="submit"
                    className="w-full font-semibold"
                    tabIndex={3}
                    disabled={form.formState.isSubmitting || !form.formState.isValid}
                >
                    Log in
                </Button>
                <p className="text-center text-sm">
                    Don't have an account?&nbsp;
                    <Link
                        href="/auth/register"
                        className="cursor-pointer font-semibold underline"
                    >
                        Register
                    </Link>
                </p>
            </form>
        </Form>
    );
};
