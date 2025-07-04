"use client";

import React from "react";
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import Link from "next/link";

import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { PasswordInput } from "@/app/auth/_components/PasswordInput";
import { Button } from "@/components/ui/button";

import { Loader2Icon } from "lucide-react";

const formSchema = z.object({
    username: z.string(),
    email: z.string().email(),
    password: z.string(),
});

export const RegisterForm = () => {
    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            username: "",
            email: "",
            password: "",
        },
        mode: "all",
    });

    async function onSubmit(values: z.infer<typeof formSchema>) {
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
                    name="username"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>
                                <span>
                                    Username<sup className="text-sm text-rose-800">*</sup>
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
                                    tabIndex={2}
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

                <Button
                    type="submit"
                    className="w-full font-semibold"
                    tabIndex={4}
                    disabled={form.formState.isSubmitting || !form.formState.isValid}
                >
                    {form.formState.isSubmitting ? (
                        <Loader2Icon className="repeat-infinite animate-spin" />
                    ) : (
                        "Register"
                    )}
                </Button>
                <p className="text-center text-xs md:text-sm">
                    Already have an account?&nbsp;
                    <Link
                        href="/auth/login"
                        className="cursor-pointer font-semibold underline"
                        prefetch={false}
                    >
                        Log in
                    </Link>
                </p>
            </form>
        </Form>
    );
};
