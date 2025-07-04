import React from "react";
import { Metadata } from "next";

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { LoginForm } from "@/app/auth/_components/LoginForm";
import { LoginRegisterCardFooter } from "@/app/auth/_components/LoginRegisterCardFooter";

export const metadata: Metadata = {
    title: "Discover | Log In",
    description: "Discover | Log In",
};

function LoginPage() {
    return (
        <div className="grid place-content-center px-2 md:px-0">
            <Card className="w-full md:w-md">
                <CardHeader className="text-center">
                    <CardTitle className="text-lg">Welcome Back to Discover</CardTitle>
                    <CardDescription className="italic">
                        Continue discovering great products and exclusive offers.
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    <LoginForm />
                </CardContent>
                <Separator />
                <LoginRegisterCardFooter />
            </Card>
        </div>
    );
}

export default LoginPage;
