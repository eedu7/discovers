import React from "react";
import { Metadata } from "next";

import { LoginRegisterCardFooter } from "@/app/auth/_components/LoginRegisterCardFooter";
import { RegisterForm } from "@/app/auth/_components/RegisterForm";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";

export const metadata: Metadata = {
    title: "Discover | Register",
    description: "Discover | Register",
};

function RegisterPage() {
    return (
        <div className="grid place-content-center px-2 md:px-0">
            <Card className="w-full md:w-md">
                <CardHeader>
                    <CardTitle>Register</CardTitle>
                </CardHeader>
                <CardContent>
                    <RegisterForm />
                </CardContent>
                <Separator />
                <LoginRegisterCardFooter />
            </Card>
        </div>
    );
}

export default RegisterPage;
